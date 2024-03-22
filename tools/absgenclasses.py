#!/usr/bin/env python3
__doc__ = '''generate linking classes for abs projects from glyph_data.csv'''
__url__ = 'https://github.com/silnrsi/font-arab-tools'
__copyright__ = 'Copyright (c) 2018-2024 SIL International  (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

import re
from silfont.core import execute
from palaso.unicode.ucd import get_ucd, loadxml
from lxml import etree
from collections import OrderedDict

argspec = [
    ('ifont', {'help': 'Input UFO'}, {'type': 'infont'}),
    ('output', {'help': 'Output filename (for new/merged classes in XML format)'}, {}),
    ('-i', '--input', {'help': 'Glyph info csv file'}, {'type': 'incsv', 'def': 'glyph_data.csv'}),
    ('--ucdxml', {'help': 'File with UCD XML data for chars in the pipeline'}, {}),
    ('-c', '--classfile', {'help': 'Input classes XML file'}, {}),
    ('-l', '--log', {'help': 'Set log file name'}, {'type': 'outfile', 'def': '_classes.log'}),
]

# UTR53 Modifier Combining Marks (from https://www.unicode.org/reports/tr53/)
mcm = {
    0x0654, # ARABIC HAMZA ABOVE
    0x0655, # ARABIC HAMZA BELOW
    0x0658, # ARABIC MARK NOON GHUNNA
    0x06DC, # ARABIC SMALL HIGH SEEN
    0x06E3, # ARABIC SMALL LOW SEEN
    0x06E7, # ARABIC SMALL HIGH YEH
    0x06E8, # ARABIC SMALL HIGH NOON
    0x08CA, # ARABIC SMALL HIGH FARSI YEH
    0x08CB, # ARABIC SMALL HIGH YEH BARREE WITH TWO DOTS BELOW
    0x08CD, # ARABIC SMALL HIGH ZAH
    0x08CE, # ARABIC LARGE ROUND DOT ABOVE
    0x08CF, # ARABIC LARGE ROUND DOT BELOW    
    0x08D3, # ARABIC SMALL LOW WAW
    0x08F3, # ARABIC SMALL HIGH WAW
}

# --------------------
# This tool works in two modes:
#
# Mode1: Without `-c`, it writes a valid classes xml file containing just the auto-generated classes (along
#        with some comments) to the output. The file can be used as-is or segments cut and pasted into a project file.
#
# Mode2: With `-c`, it reads the named classes xml file and any classes named therein that are
#        computed by the program are replaced. In this case the only comments added are the "autogenerated"
#        comment associated with each replaced class.
#
# To accommodate both modes, the program builds an ordered sequence (actually ordered dictionary) of all
# the text elements (other than the enclosing `<classes>..</classes>`) element needed to accomplish (2).
# Then:
#  - In Mode1 (-c is not supplied) the tool joins the all text segments together, along with the enclosing
#    `classes` element and writes them to the output.
#  - In Mode2 (-c is supplied), the tool parses the xml file and then uses etree.fromstring() to create sub-elements
#    to replace ones in the parsed file.
# --------------------


def doit(args):
    logger = args.logger

    if args.ucdxml:
        # Update UCD module with data for relevant pipeline chars 
        loadxml(args.ucdxml)

    # Iterate over glyph_data file looking for:
    #   Encoded glyphs whose USV shows they are Right- or Dual-joining
    #     Warn if their name has an extension
    #     Keep a list of right-joining and a list of dual-joining
    #  Arabic mark glyphs
    #     Keep lists needed for UTF53 processing
    #

    # Ordered Dictionary to hold generated xml source fragments. Any fragment that represents
    # a glyph class must encode a valid xml subtree, so neither leading nor trailing whitespace are allowed.
    # Other elements (such as comments added by addAnonomousElement()) can include arbitrary whitespace,
    # but see default indent variable below.
    newClassesXML = OrderedDict()  # classname:classXMLstr, in order generated

    def addAnonomousElement(s):
        """ add a non-class element (typically comments to be included for Mode1) """
        # we make up a key based on current length of the dictionary
        newClassesXML[f'anon#{len(newClassesXML)}'] = s

    # default indent string ("n-dent")
    # In Mode2 this string will be replaced by the indent string of the first <class> object.
    # In Mode1 then `f'\n\n{nd}'.join(...)` will be used to concatenate all data from newClassesXML
    nd = '    '   # Note that by default f'{nd}' is same length as nd

    nClasses = 0    # Keep track of number of classes generated

    # For all glyphs:
    basename2uid = {}   # Mapping basename to USV for encoded chars
    ligature2uids = {}  # Mapping basename to USV list for ligatures
    glyphOrder = {}     # dictionary to record sort order of glyphs
    ufomissing = set()  # glyphs mentioned or needed in csv that aren't in UFO

    # Sets needed for class generation
    rjoining = set()    # names of all right-joining encoded glyphs
    djoining = set()    # names of all dual-joining encoded glyphs
    lams = set()        # lam-like
    alefs = set()       # alef-like
    alefsRare = set()   # alef-like from Unicode 14 (U+0870 .. U+0882)
    rehs = set()        # reh-like
    waws = set()        # waw-like
    takesLargeAlef = set()  # has bowl (final yehs, seens, etc)

    # Sets of mark glyphs needed for UTR53
    utr53_220MCM = set()
    utr53_230MCM = set()
    utr53_shadda = set()
    utr53_fixedPos = set()
    utr53_alef = set()
    utr53_220other = set()
    utr53_230other = set()

    # needed for re-processing an existing classes xml file:
    classes = None  # root class of existing xml file, set only if args.classfile provided.

    def splitgname(gname):
        """split a glyph name into base and extension (possibly None) unless the name starts with '.' """
        p = gname.find('.')
        return (gname, None) if p <= 0 else (gname[0:p], gname[p:])

    def addMark(gname, uid):
        """accumulate sets of mark glyphs based on combining class and MCM status"""
        ccc = int(get_ucd(uid, 'ccc'))
        if uid in mcm:
            if ccc == 220:
                utr53_220MCM.add(gname)
            elif ccc == 230:
                utr53_230MCM.add(gname)
            else:
                logger.log(f'glyph {gname} (uid {uid:04X}) claims to be MCM but has ccc {ccc}', 'S')
        elif ccc == 33:
            utr53_shadda.add(gname)
        elif 0 < ccc < 35:
            utr53_fixedPos.add(gname)
        elif ccc == 35:
            utr53_alef.add(gname)
        elif ccc == 220:
            utr53_220other.add(gname)
        elif ccc == 230:
            utr53_230other.add(gname)
        elif ccc != 0:
            # warn about anything else other than cgj and VS1-VS16
            logger.log(f'unexpected glyph {gname} with uid {uid:04X} and ccc {ccc}; glyph ignored', 'W')

    def addToClasses(gname, uid, basename, ext, encoded):
        """ given a glyph with its information, add it to needed classes"""
        # Note that if the glyph is not encoded, the uid will be that of the encoded variant of it.
        # Ignore anything not in arabic blocks
        if get_ucd(uid, 'blk').startswith('Arabic'):
            jt = get_ucd(uid, 'jt')
            jg = get_ucd(uid, 'jg')
            
            if jt == 'R' and encoded:
                rjoining.add(gname)
                if jg == 'Alef':
                    if 0x0870 <= uid <= 0x0882:
                        # Rare alefs:
                        alefsRare.add(gname)
                    else:
                        alefs.add(gname)
            elif jt == 'D' and encoded:
                djoining.add(gname)
                if jg == 'Lam':
                    lams.add(gname)
            elif get_ucd(uid, 'bc') == 'NSM':
                # Partition up the marks for pseudo UTR53
                addMark(gname, uid)

            if jg in ('Yeh','Farsi_Yeh', 'Yeh_With_Tail', 'Seen','Sad',) and ext in (None, ".fina"):
                takesLargeAlef.add(gname)
            elif jg == 'Reh' and encoded:
                rehs.add(gname)
            elif jg == 'Waw' and encoded:
                waws.add(gname)

            if gname not in args.ifont:
                ufomissing.add(gname)

    def makeLines(glist, padding=0):
        """break list of glyphnames into lines for output"""
        lines = []
        while len(glist):
            line = []
            linelgt = 0
            while len(glist) and linelgt < 120:
                gname = glist.pop(0)
                line.append(gname)
                linelgt += len(gname) + 1 + padding # Allow for space in between, and .xxxx extension
            if len(line):
                lines.append(line)
        return lines

    def outputMatchingClasses(cname, glist, related=None, exts=None):
        """add a class, or group of related classes, to newClassesXML dictionary, checking glyph orders"""
        # cname = name of first (possibly only) class to output
        # glist = list of glyph names of the first class
        # related = list of 2-tuples that identify classes that should parallel the first class in correct order
        #    each tuple contains (rname, extension) where
        #        rname = name of the related class
        #        extension = glyphname extension to add to members of cname (e.g., ".init")
        nonlocal nClasses
        numClasses = 1 if related is None else 1+len(related)
        exts = '' if exts is None else f" exts='{exts}'"
        if numClasses == 1:
            padding = 0
        else:
            # Lots of work to do in dealing with related classes (e.g., right-joining and their finals):
            # preliminaries:
            addAnonomousElement(f'<!-- *NEXT {numClasses} CLASSES MUST MATCH* -->')
            # Classes will be line-wrapped such that the same glyph names appear in each line of the related classes.
            # To do this we need to know what the longest extension is in the related classes and account for it
            # when line-wrapping the first class.
            padding = max(len(r[1]) for r in related)
            # sort glist by glyphorder:
            glist = sorted(glist, key=lambda x: glyphOrder[x])
            # for each related class, verify the corresponding glyphs are present and in the same glyph order in the font
            for r in related:
                (rname, ext) = r
                rlist = (f'{x}{ext}' for x in glist)
                # Check for missing or out-of-order glyphs
                lastGlyphOrder = None
                csvmissing = set()
                outOfOrder = set()
                for gname in rlist:
                    try:
                        myOrder = glyphOrder[gname]
                        if lastGlyphOrder is not None and myOrder <= lastGlyphOrder:
                            outOfOrder.add(gname)
                        lastGlyphOrder = myOrder
                    except KeyError:
                        csvmissing.add(gname)
                    if gname not in args.ifont:
                        ufomissing.add(gname)
                if len(csvmissing):
                    logger.log(f'CSV is missing glyphs for class {rname}: {" ".join(sorted(csvmissing))}', 'E')
                if len(outOfOrder):
                    logger.log(f'Out of order glyphs for class {rname}: {" ".join(sorted(outOfOrder))}', 'E')
        # finally we can output classes, with glyphs in alphabetical order
        glist = sorted(glist)
        nglyphs = len(glist)
        lines = makeLines(glist, padding)
        s = '' if numClasses == 1 else f': 1 of {numClasses}'

        xml = f"<class name='{cname}'{exts}>    <!-- autogenerated{s} ({nglyphs} glyphs) -->\n"
        for line in lines:
            xml += f"{nd}{nd}{' '.join(line)}\n"
        xml += f'{nd}</class>'
        newClassesXML[cname] = xml

        if numClasses > 1:
            for i, r in enumerate(related):
                (rname, ext) = r
                xml = f"<class name='{rname}'>    <!-- autogenerated: {i+2} of {numClasses} ({nglyphs} glyphs) -->\n"
                for line in lines:
                    xml += f"{nd}{nd}{' '.join(f'{x}{ext}' for x in line)}\n"
                xml += f'{nd}</class>'
                newClassesXML[rname] = xml
        nClasses += numClasses

    ##############################
    # Step 1: Get headings from input csvfile:

    incsv = args.input
    fl = incsv.firstline
    if fl is None: logger.log('Empty input file', 'S')
    # required columns:
    try:
        nameCol = fl.index('glyph_name')
        usvCol = fl.index('USV')
        orderCol = fl.index('DesignerOrder')
    except ValueError as err:
        logger.log('Missing csv input field: ' + str(err), 'S')
    except Exception as err:
        logger.log('Error reading csv input field: ' + str(err), 'S')
    next(incsv.reader, None)  # Skip first line with headers in

    ##############################
    # Step 2: read CSV data and build classes contents as we go:

    # RE that matches USV sequences for ligatures
    ligatureRE = re.compile('^[0-9A-Fa-f]{4,6}(?:_[0-9A-Fa-f]{4,6})+$')
    
    # RE that matches space-separated USV sequences
    USVsRE = re.compile('^[0-9A-Fa-f]{4,6}(?:\s+[0-9A-Fa-f]{4,6})*$')

    # Process all records in glyph_data
    for line in incsv:
        gname = line[nameCol].strip()

        # things to ignore:
        if len(gname) == 0:
            logger.log('empty glyph name in glyph_data; ignored', 'W')
            continue
        if re.match('[#._]|nonmarkingreturn|tab|absAutoKashida', gname):
            continue

        # remember glyph ordering for all glyphs
        glyphOrder[gname] = float(line[orderCol])
        # split gname
        basename, ext = splitgname(gname)

        # Process USV
        # could be empty string, or an underscore- or space-separated list of USVs
        usvs = line[usvCol].strip()
        if len(usvs) == 0:
            # Empty USV field, unencoded glyph
            usvs = ()
        elif USVsRE.match(usvs):
            # space-separated hex values:
            usvs = usvs.split()
            isLigature = False
        elif ligatureRE.match(usvs):
            # '_' separated hex values (ligatures)
            usvs = usvs.split('_')
            isLigature = True
        else:
            logger.log(f'glyph_data line {incsv.line_num}: invalid USV field "{usvs}"; ignored', 'W')
            usvs = ()
        uids = [int(x, 16) for x in usvs]

        if len(uids) == 0:
            # Handle unencoded glyphs
            # for now we're ignoring variants of ligatures:
            if basename in ligature2uids:
                continue
            # for everything else, we should have seen the encoded variant already,
            # so act based on its uid:
            try:
                uid = basename2uid[basename]
                addToClasses(gname, uid, basename, ext, False)
            except KeyError:
                logger.log(f'cannot determine USV for unencoded glyph {gname}; glyph ignored', 'E')
        elif not isLigature:
            # Handle simple encoded glyphs
            # TODO: What should we do if glyph has multiple encodings? Right now just take first
            uid = uids[0]
            basename2uid[basename] = uid
            if ext is not None:
                logger.log(f'encoded glyph {gname} has extensions -- be sure to check construction of variant forms', 'E')
            addToClasses(gname, uid, basename, ext, True)
        else:
            # Handle ligature glyphs
            ligature2uids[basename] = uids
            # otherwise, for now, we're ignoring ligatures

    ##############################
    # Step 4: figure out what the indent string should be:

    if args.classfile:
        # In this mode we read parse an existing classes.xml file, replacing
        # any class definitions that we know about, then write the result to args.output

        with open(args.classfile,'r', encoding='utf-8') as f:
            tree = etree.parse(f)
        classes = tree.getroot()  # root of document is <classes>
        # find indent of the first sub-element of the tree,
        # i.e. the final space-or-tab sequence of the root element:
        m = re.search(r'[ \t]+$', classes.text)
        nd = m.group(0) if m else '    '

    ##############################
    # Step 5: Compute all output, even if missing or out of order

    addAnonomousElement(f'<!-- ***** NB: The following classes were generated algorithmically \n'
                        f'{nd} based on Unicode properties (see tools/absgenclasses.py) ***** -->')

    addAnonomousElement('<!--\n' +
        f'{nd}===============================\n' +
        f'{nd}Linking form\n' +
        f'{nd}===============================\n' +
        f'{nd}-->')

    outputMatchingClasses('DualLinkIsol', djoining,
                          (('DualLinkInit', '.init'), ('DualLinkMedi', '.medi'), ('DualLinkFina', '.fina')))
    outputMatchingClasses('RightLinkIsol', rjoining,
                          (('RightLinkFina', '.fina'),))

    outputMatchingClasses('LamIso', lams,
                        (('LamIni', '.init'), ('LamMed', '.medi'), ('LamFin', '.fina')))
    outputMatchingClasses('AlefIso', alefs,
                        (('AlefFin', '.fina'),))

    # TODO: autogenerate rare-alef and  lam-alef classes

    # the UTR53 classes:
    addAnonomousElement('<!--\n' 
        f'{nd}===============================\n'
        f'{nd}For pseudo-UTR53 implementation\n' 
        f'{nd}===============================\n'
        f'{nd}-->')

    for clname, glist in zip(('UTR53_220MCM', 'UTR53_230MCM', 'UTR53_shadda', 'UTR53_fixedPos', 'UTR53_alef', 'UTR53_220other', 'UTR53_230other'),
                             (utr53_220MCM, utr53_230MCM, utr53_shadda, utr53_fixedPos, utr53_alef, utr53_220other, utr53_230other)):
        outputMatchingClasses(clname, glist)

    addAnonomousElement('<!--\n' 
        f'{nd}===============================\n'
        f'{nd}Miscellaneous\n' 
        f'{nd}===============================\n'
        f'{nd}-->')

    outputMatchingClasses('TakesLargeDaggerAlef', takesLargeAlef)
    outputMatchingClasses('RehAll', rehs, exts='.fina')
    outputMatchingClasses('WawAll', waws, exts='.fina')

    ##############################
    # Step 6: write new (or update existing) classes file:

    if classes is not None:
        # We're in Mode2
        nClasses = 0  # count only classes actually updated
        for cname, s in newClassesXML.items():
            if cname.startswith('anon#'):
                continue
            # See if this cname is in the input classes.xml file
            elList = classes.xpath(f'class[@name="{cname}"]')
            if not len(elList):
                # TODO insert related classes if needed
                continue
            elif len(elList) > 1:
                logger.log(f'Class named {cname} occurs more than once in "{args.classfile}"', "E")

            logger.log(f'Updating class {cname}', 'I')
            # retrieve index of this element:
            i = classes.getchildren().index(elList[0])
            # Replace this element.
            newEl = etree.fromstring(s)
            newEl.tail = f'\n\n{nd}'
            classes[i] = newEl
            nClasses += 1

        # Now we can rebuild the text representation of the tree
        # I would like to be able to do, simply:
        #    newXML = etree.tostring(tree, encoding='utf-8', xml_declaration=True)
        # however lxml removes the "tail" from all siblings of the root element (search for "automatically discarded"
        # in https://lxml.de/apidoc/lxml.etree.html). This means that if there are comments before or after the
        # the root <classes>...</classes> element, any whitespace (such as linebreaks or indents) following such
        # comments will be removed :-(
        #
        # Rather than live with this, we reconstruct such comment text and assume '\n\n' separators:
        # (Note that itersiblings() retrieves preceding siblings in reverse order)
        prefix = [etree.tostring(i, encoding='unicode') + '\n\n' for i in classes.itersiblings(tag=None, preceding=True)]
        prefix.reverse()
        prefix = ''.join(prefix)
        suffix = ''.join('\n\n' + etree.tostring(i, encoding='unicode') for i in classes.itersiblings(tag=None, preceding=False))
        newXML = f"{prefix}{etree.tostring(classes, encoding='unicode')}{suffix}\n"

    else:
        newXML = f'<classes>\n\n{nd}' + f'\n\n{nd}'.join(newClassesXML.values()) + '\n\n</classes>\n'

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("<?xml version='1.0' encoding='utf-8'?>\n\n")
        f.write(newXML)

    if classes is not None:
        logger.log(f'{nClasses} classes updated in {args.output}.', 'P')
    else:
        logger.log(f'{nClasses} classes written to {args.output}. Not all that were output are necessarily needed ' +
               'in every project; manually copy those that are into source/classes.xml.', 'P')

    if len(ufomissing):
        logger.log(f'UFO is missing glyphs: {" ".join(sorted(ufomissing))}', 'W')

def cmd(): execute('FP', doit, argspec)
if __name__ == '__main__': cmd()

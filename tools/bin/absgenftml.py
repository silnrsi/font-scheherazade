#!/usr/bin/python3
'generate ftml tests from glyph_data.csv and UFO'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2018,2020 SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

import re
from silfont.core import execute
import silfont.ftml_builder as FB
from palaso.unicode.ucd import get_ucd

argspec = [
    ('ifont', {'help': 'Input UFO'}, {'type': 'infont'}),
    ('output', {'help': 'Output file ftml in XML format', 'nargs': '?'}, {'type': 'outfile', 'def': '_out.ftml'}),
    ('-i','--input', {'help': 'Glyph info csv file'}, {'type': 'incsv', 'def': 'glyph_data.csv'}),
    ('-f','--fontcode', {'help': 'letter to filter for glyph_data'},{}),
    ('-l','--log', {'help': 'Set log file name'}, {'type': 'outfile', 'def': '_ftml.log'}),
    ('--langs', {'help':'List of bcp47 language tags', 'default': None}, {}),
    ('--rtl', {'help': 'enable right-to-left features', 'action': 'store_true'}, {}),
    ('--norendercheck', {'help': 'do not include the RenderingUnknown check', 'action': 'store_true'}, {}),
    ('-t', '--test', {'help': 'name of the test to generate', 'default': None}, {}),
    ('-s','--fontsrc', {'help': 'font source: "url()" or "local()" optionally followed by "=label"', 'action': 'append'}, {}),
    ('--scale', {'help': 'percentage to scale rendered text (default 100)'}, {}),
    ('--ap', {'help': 'regular expression describing APs to examine', 'default': '.'}, {}),
    ('-w', '--width', {'help': 'total width of all <string> column (default automatic)'}, {}),
    ('--xsl', {'help': 'XSL stylesheet to use'}, {}),
]


joinGroupKeys = {
    'Ain' : 1,
    'Alef' : 2,
    'Beh' : 3,
    'Yeh' : 4, 'Farsi_Yeh' : 4, # Near Beh Due To Medial Form
    'Noon' :5, 'African_Noon' : 5,  # Near Yeh Due To Medial Form
    'Nya' : 6,  # Near Noon Due To Final Form
    'Sad' : 7,  # Near Noon Due To Final Form
    'Seen' : 8,
    'Yeh_With_Tail' : 9,
    'Rohingya_Yeh' : 10,
    'Yeh_Barree' : 11, 'Burushaski_Yeh_Barree' : 11,
    'Dal' : 12,
    'Feh' : 13, 'African_Feh' : 13,
    'Kaf' : 14,
    'Gaf' : 15,
    'Swash_Kaf' : 16,
    'Hah' : 17,
    'Heh' : 18,
    'Heh_Goal' : 19,
    'Teh_Marbuta' : 20, 'Teh_Marbuta_Goal' : 20,
    'Knotted_Heh' :21,
    'Lam' : 22,
    'Meem' : 23,
    'Qaf' : 24, 'African_Qaf' : 24,
    'Reh' : 25 ,
    'Tah' : 26,
    'Waw' : 27,
    'Straight_Waw' : 28,
}

def joinGoupSortKey(uid:int):
    return joinGroupKeys.get(get_ucd(uid, 'jg'), 99) * 65536 + uid

ageToFlag = 13.0
ageColor = "#FFE0E0"  # very light red

def doit(args):
    logger = args.logger

    # Read input csv
    builder = FB.FTMLBuilder(logger, incsv=args.input, fontcode=args.fontcode, font=args.ifont, ap=args.ap,
                             rtlenable=True, langs=args.langs)

    # Override default base (25CC) for displaying combining marks
    builder.diacBase = 0x0628   # beh

    def basenameSortKey(uid:int):
        return builder.char(uid).basename.lower()

    # Initialize FTML document:
    test = args.test or "AllChars (NG)"  # Default to AllChars
    widths = None
    if args.width:
        try:
            width, units = re.match(r'(\d+)(.*)$', args.width).groups()
            if len(args.fontsrc):
                width = int(round(int(width)/len(args.fontsrc)))
            widths = {'string': f'{width}{units}'}
        except:
            logger.log('Unable to parse width argument "{args.width}"', 'W')
    # split labels from fontsource parameter
    fontsrc = []
    labels = []
    for sl in args.fontsrc:
        try:
            s, l = sl.split('=',1)
            fontsrc.append(s)
            labels.append(l)
        except ValueError:
            fontsrc.append(sl)
            labels.append(None)
    ftml = FB.FTML(test, logger, rendercheck=not args.norendercheck, fontscale=args.scale, widths=widths,
                   xslfn=args.xsl, fontsrc=fontsrc, fontlabel=labels, defaultrtl=args.rtl)

    def flagUnicodeVersion(uids):
        # if any uid in uids has Unicode age >= ageToFlag, then set the test background color to ageColor
        if max(map(lambda x: float(get_ucd(x, 'age')), uids)) >= ageToFlag:
            ftml.setBackground(ageColor)

    if test.lower().startswith("allchars"):
        # all chars that should be in the font:
        ftml.startTestGroup('Encoded characters')
        for uid in sorted(builder.uids()):
            if uid < 32: continue
            c = builder.char(uid)
            flagUnicodeVersion((uid,))
            for featlist in builder.permuteFeatures(uids=(uid,)):
                ftml.setFeatures(featlist)
                builder.render((uid,), ftml)
            ftml.clearFeatures()
            if len(c.langs):
                for langID in builder.allLangs:
                    ftml.setLang(langID)
                    builder.render((uid,), ftml)
                ftml.clearLang()
            ftml.clearBackground()

        # Add specials and ligatures that were in the glyph_data:
        ftml.startTestGroup('Specials & ligatures from glyph_data')
        for basename in sorted(builder.specials()):
            special = builder.special(basename)
            flagUnicodeVersion(special.uids)
            for featlist in builder.permuteFeatures(uids=special.uids, feats=special.feats):
                ftml.setFeatures(featlist)
                builder.render(special.uids, ftml)
                ftml.closeTest()
            ftml.clearFeatures()
            if len(special.langs):
                for langID in builder.allLangs:
                    ftml.setLang(langID)
                    builder.render(special.uids, ftml)
                    ftml.closeTest()
                ftml.clearLang()
            ftml.clearBackground()

        # Add Lam-Alef data manually
        ftml.startTestGroup('Lam-Alef')
        lamlist = sorted(filter(lambda uid: get_ucd(uid,'jg') == 'Lam', builder.uids()))
        aleflist = sorted(filter(lambda uid: get_ucd(uid,'jg') == 'Alef', builder.uids()))
        for lam in lamlist:
            for alef in aleflist:
                flagUnicodeVersion((lam, alef))
                for featlist in builder.permuteFeatures(uids=(lam, alef)):
                    ftml.setFeatures(featlist)
                    builder.render((lam, alef), ftml)
                    ftml.closeTest()
                ftml.clearFeatures()
                if lam == 0x0644 and 'cv02' in builder.features:
                    # Also test lam with hamza above for warsh variants
                    for featlist in builder.permuteFeatures(uids=(lam, 0x0654, alef), feats=('cv02',)):
                        ftml.setFeatures(featlist)
                        builder.render((lam, 0x0654, alef), ftml)
                        ftml.closeTest()
                    ftml.clearFeatures()
                ftml.clearBackground()

        # Add Allah data manually
        ftml.startTestGroup('Allah ligatures')
        ftml.addToTest(0xFDF2, r"\uFDF2", comment="Rule 1")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0641\u0644\u0644\u0647", label="f-l-l-h", comment="shouldn't match")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u0651\u0670\u0647", label="a-l-l-s-da-hf", comment="Rule 2 (daggeralef)")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u0670\u0651\u0647", label="a-l-l-da-s-hf")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u0651\u0670\u06C1", label="a-l-l-s-da-hgf")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u0670\u0651\u06C1", label="a-l-l-da-s-hgf")
        ftml.closeTest()

        ftml.addToTest(None, r"\u0627\u0644\u0644\u0651\u064E\u0647", label="a-l-l-s-f-hf", comment="Rule 2 (fatha)")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u064E\u0651\u0647", label="a-l-l-f-s-hf")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u0651\u064E\u06C1", label="a-l-l-s-f-hgf")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u0644\u064E\u0651\u06C1", label="a-l-l-f-s-hgf")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u06EB\u0644\u064E\u0651\u06C1", label="a-l-M-l-s-da-hgf", comment="Rule 2c: shouldn't match")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0641\u0644\u0644\u064E\u0651\u06C1", label="f-l-l-s-da-hgf", comment="Rule 2d: non-alef")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0641\u0627\u0644\u0644\u064E\u0651\u06C1", label="f-a-l-l-s-da-hgf", comment="Rule 2d: not isolate alef")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u06EB\u0644\u0644\u064E\u0651\u06C1", label="a-M-l-l-s-da-hgf", comment="Rule 2d: Mark")
        ftml.closeTest()
        ftml.addToTest(None, r" \u0644\u0644\u0651\u064E\u0647", label="space-l-l-s-da-hf", comment="Rule 2d: shouldn't match")
        ftml.closeTest()

        ftml.addToTest(None, r"\u0627\u0644\u0644\u0647", label="a-l-l-h", comment="Rule 3")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0622\u0644\u0644\u0647", label="aM-l-l-h")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0623\u0644\u0644\u0647", label="aH-l-l-h")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0671\u0644\u0644\u0647", label="aW-l-l-h", comment="won't work")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u06EB\u0644\u0644\u0647", label="a-M-l-l-h")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0641\u0627\u0644\u0644\u0647", label="f-a-l-l-h", comment="Rule 3a: shouldn't match")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u06EB\u0644\u0647", label="a-l-M-l-h", comment="Rule 3d: shouldn't match")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u200D\u0644\u0647", label="a-l-zwj-l-h", comment="Rule 4a: shouldn't match")
        ftml.closeTest()
        ftml.addToTest(None, r"\u0627\u0644\u200D\u0644\u0651\u0670\u0647", label="a-l-zwj-l-s-da-h", comment="Rule 4a: shouldn't match")
        ftml.closeTest()

    if test.lower().startswith("al sorted"):
        # all AL chars, sorted by shape:
        ftml.startTestGroup('Arabic Letters')
        for uid in sorted(filter(lambda u: get_ucd(u, 'bc') == 'AL', builder.uids()), key=joinGoupSortKey):
            c = builder.char(uid)
            flagUnicodeVersion((uid,))
            for featlist in builder.permuteFeatures(uids=(uid,)):
                ftml.setFeatures(featlist)
                builder.render((uid,), ftml)
            ftml.clearFeatures()
            if len(c.langs):
                for langID in builder.allLangs:
                    ftml.setLang(langID)
                    builder.render((uid,), ftml)
                ftml.clearLang()
            ftml.clearBackground()

    if test.lower().startswith("diac"):
        # Diac attachment:

        doLongTest = 'short' not in test.lower()

        # Representative base and diac chars:
        if doLongTest:
            repDiac = list(filter(lambda x: x in builder.uids(), (0x064E, 0x0650, 0x065E, 0x0670, 0x0616, 0x06E3, 0x08F0, 0x08F2)))
            repBase = list(filter(lambda x: x in builder.uids(), (0x0627, 0x0628, 0x062B, 0x0647, 0x064A, 0x77F, 0x08AC)))
            lamlist = list(filter(lambda x: x in builder.uids(), (0x0644, 0x06B5, 0x06B6, 0x06B7, 0x06B8, 0x076A, 0x08A6)))
            aleflist = list(filter(lambda x: x in builder.uids(), (0x0627, 0x0622, 0x0623, 0x0625, 0x0671, 0x0672, 0x0673, 0x0675, 0x0773, 0x0774)))
        else:
            repDiac = list(filter(lambda x: x in builder.uids(), (0x064E, 0x0650, 0x0654, 0x0670)))
            repBase = list(filter(lambda x: x in builder.uids(), (0x0627, 0x0628)))
            lamlist = list(filter(lambda x: x in builder.uids(), (0x0644, 0x06B5, 0x06B6, 0x06B7, 0x06B8, 0x076A, 0x08A6)))
            aleflist = list(filter(lambda x: x in builder.uids(), (0x0627, 0x0622, 0x0623, 0x0625, 0x0671, 0x0672, 0x0673, 0x0675, 0x0773, 0x0774)))

        ftml.startTestGroup('Representative diacritics on all bases that take diacritics')
        for uid in sorted(builder.uids()):
            if uid < 32 or uid in (0xAA, 0xBA): continue
            c = builder.char(uid)
            # Always process Lo, but others only if that take marks:
            if c.general == 'Lo' or c.isBase:
                for diac in repDiac:
                    flagUnicodeVersion((uid,diac))
                    for featlist in builder.permuteFeatures(uids=(uid,diac)):
                        ftml.setFeatures(featlist)
                        builder.render((uid,diac), ftml, addBreaks=False, dualJoinMode=2)
                        if doLongTest:
                            if diac != 0x0651:  # If not shadda
                                # include shadda, in either order:
                                builder.render((uid, diac, 0x0651), ftml, addBreaks=False, dualJoinMode=2)
                                builder.render((uid, 0x0651, diac), ftml, addBreaks=False, dualJoinMode=2)
                            if diac != 0x0654:  # If not hamza above
                                # include hamza above, in either order:
                                builder.render((uid, diac, 0x0654), ftml, addBreaks=False, dualJoinMode=2)
                                builder.render((uid, 0x0654, diac), ftml, addBreaks=False, dualJoinMode=2)
                    ftml.clearFeatures()
                    ftml.clearBackground()
                ftml.closeTest()

        ftml.startTestGroup('All Arabic diacritics on representative bases')
        for uid in sorted(builder.uids()):
            # ignore non-ABS marks
            if uid < 0x600 or uid in range(0xFE00, 0xFE10): continue
            c = builder.char(uid)
            if c.general == 'Mn':
                for base in repBase:
                    flagUnicodeVersion((uid,base))
                    for featlist in builder.permuteFeatures(uids=(uid,base)):
                        ftml.setFeatures(featlist)
                        builder.render((base,uid), ftml, keyUID=uid, addBreaks=False, dualJoinMode=2)
                        if doLongTest:
                            if uid != 0x0651: # if not shadda
                                # include shadda, in either order:
                                builder.render((base, uid, 0x0651), ftml, keyUID=uid, addBreaks=False, dualJoinMode=2)
                                builder.render((base, 0x0651, uid), ftml, keyUID=uid, addBreaks=False, dualJoinMode=2)
                            if diac != 0x0670:  # If not superscript alef
                                # include superscript alef, in either order:
                                builder.render((uid, diac, 0x0670), ftml, addBreaks=False, dualJoinMode=2)
                                builder.render((uid, 0x0670, diac), ftml, addBreaks=False, dualJoinMode=2)
                    ftml.clearFeatures()
                    ftml.clearBackground()
                ftml.closeTest()

        ftml.startTestGroup('Special cases')
        builder.render((0x064A, 0x064E), ftml)   # Yeh + Fatha should keep dots
        builder.render((0x064A, 0x0654), ftml)   # Yeh + Hamza should loose dots
        ftml.closeTest()

        ftml.startTestGroup('LamAlef ligatures')
        diaB = 0x064D
        diaA = 0x064B
        for lam in lamlist:
            for alef in aleflist:
                flagUnicodeVersion((lam,alef))
                for featlist in builder.permuteFeatures(uids=(lam,alef)):
                    ftml.setFeatures(featlist)
                    builder.render((lam, alef),             ftml, addBreaks=False)
                    builder.render((lam, diaA, alef, diaA), ftml, addBreaks=False)
                    builder.render((lam, diaB, alef),       ftml, addBreaks=False)
                    builder.render((lam, alef, diaB),       ftml, addBreaks=False)
                    builder.render((lam, diaB, alef, diaB), ftml, addBreaks=False)
                ftml.clearFeatures()
                ftml.clearBackground()
                ftml.closeTest()

    if test.lower().startswith("subtending"):
        # Generates sample data for all subtending marks. Data includes sequences of 0 to n+1
        # digits, where n is the maximum expected to be supported on the mark. Latin, Arbic-Indic,
        # and Extended Arabic-Indic digits are included.
        for digitSample in filter(lambda x: x in builder.uids(), (0x0032, 0x0668, 0x06F8)):
            digitOne = (digitSample & 0xFFF0) + 1
            for uid,lgt in filter(lambda x: x[0] in builder.uids(), ([0x600,3], [0x0601,4], [0x0602,2], [0x0603,4], [0x0604,4], [0x0605,4], [0x06DD,3])):
                c = chr(uid)
                label = "U+{0:04X} {1}".format(uid, 'latn' if digitOne == 0x0031 else 'arab' if digitOne == 0x0661 else 'urdu')
                comment = builder.char(uid).basename
                flagUnicodeVersion((uid,))
                for featlist in builder.permuteFeatures(uids=(uid,)):
                    ftml.setFeatures(featlist)
                    ftml.addToTest(uid, "\u0628" + c + "\u0645", label, comment)
                    for ln in range(1,lgt+1):
                        ftml.addToTest(uid, c + chr(digitSample)*ln)
                    ftml.addToTest(uid, c + chr(digitOne) + chr(digitOne+1))
                ftml.clearFeatures()
                ftml.closeTest()
                ftml.clearBackground()

                if uid == 0x06DD and digitOne == 0x06F1:
                    # Extra items for Eastern digits
                    flagUnicodeVersion((uid,))
                    for featlist in builder.permuteFeatures(uids=(uid, 0x06F7)):
                        ftml.setFeatures(featlist)
                        ftml.addToTest(uid, c + "\u06F4\u06F6\u06F7", label, "4 6 7")
                    ftml.clearFeatures()
                    for langID in builder.allLangs:
                        ftml.setLang(langID)
                        for featlist in ((None,), (['cv80', '1'],),  (['cv80', '2'],)):
                            ftml.setFeatures(featlist)
                            ftml.addToTest(uid, c + "\u06F4\u06F6\u06F7", label, "4 6 7")
                        ftml.clearFeatures()
                    ftml.clearLang()
                    ftml.closeTest()
                    ftml.clearBackground()

    if test.lower().startswith("showinv"):
        # Sample data for chars that have a "show invisible" feature
        # The 'r', 'a', 'ra' indicates whether this is standard in Roman fonts, Arabic fonts, or both.
        invlist = [
            (0x034F, 'r' ), (0x061C, 'a' ), (0x200B, 'r' ), (0x200C, 'ra'), (0x200D, 'ra'), (0x200E, 'ra'),
            (0x200F, 'ra'), (0x202A, 'ra'), (0x202B, 'ra'), (0x202C, 'ra'), (0x202D, 'ra'), (0x202E, 'ra'),
            (0x202E, 'r' ), (0x2060, 'r' ), (0x2061, 'r' ), (0x2062, 'r' ), (0x2063, 'r' ), (0x2066, 'a' ),
            (0x2067, 'a' ), (0x2068, 'a' ), (0x2069, 'a' ), (0xFE00, 'ra'), (0xFE01, 'ra'), (0xFE02, 'ra'),
            (0xFE03, 'ra'), (0xFE04, 'ra'), (0xFE05, 'ra'), (0xFE06, 'ra'), (0xFE07, 'ra'), (0xFE08, 'ra'),
            (0xFE09, 'ra'), (0xFE0A, 'ra'), (0xFE0B, 'ra'), (0xFE0C, 'ra'), (0xFE0D, 'ra'), (0xFE0E, 'ra'),
            (0xFE0F, 'ra')
        ]
        featlist=(('invs', '1'), ('ss06', '1'))
        ftml.setFeatures(featlist)
        for inv in invlist:
            uid = inv[0]
            c = chr(uid)
            label = 'U+{0:04X} ({1})'.format(uid, inv[1])
            comment = builder.char(uid).basename if uid in builder.uids() else ""
            ftml.addToTest(uid, " " + c + " ", label, comment)
            ftml.closeTest()
        ftml.clearFeatures()

    if test.lower().startswith('daggeralef'):
        for uid in sorted(builder.uids(), key=joinGoupSortKey):
            if get_ucd(uid,'jg') not in ('Sad', 'Seen', 'Yeh'):
                # If not Yeh, Sad or seen joining group we're not interested
                continue
            flagUnicodeVersion((uid,))
            for featlist in builder.permuteFeatures(uids=(uid, 0x0670)):
                ftml.setFeatures(featlist)
                builder.render((uid, 0x0670), ftml)
            ftml.clearFeatures()
            ftml.clearBackground()
            ftml.closeTest()

    if test.lower().startswith('kern'):
        rehs = sorted(filter(lambda uid: get_ucd(uid,'jg') == 'Reh', builder.uids()))
        waws = sorted(filter(lambda uid: get_ucd(uid,'jg') == 'Waw', builder.uids()))
        uids = sorted(filter(lambda uid: get_ucd(uid, 'jt') in ('D', 'R') or uid == 0xFD3E, builder.uids()), key=joinGoupSortKey)
        # NB: I wondered about including punctuation, i.e.,  get_ucd(uid, 'gc').startswith('P'), but the default
        #     spacing is pretty good and graphite collision avoidance makes it worse, so the only one we need is FDFE

        dbehf = chr(0x066E) + chr(0x200D)  # dotless beh final
        alef = chr(0x0627)   # alef
        zwj  = chr(0x200D)   # Zero width joiner
        ma = 0x064B     # Mark above (fathatan)
        mb = 0x064D # chr(0x064D)     # Mark below (kasratan)

        if "data" not in test.lower():
            ftml.startTestGroup('All the rehs')
            for uid in rehs:
                c = chr(uid)
                label = 'U+{0:04X}'.format(uid)
                comment = builder.char(uid).basename
                flagUnicodeVersion((uid,))
                for featlist in builder.permuteFeatures(uids=(uid,)):
                    ftml.setFeatures(featlist)
                    ftml.addToTest(uid, c + dbehf + ' ' + zwj + c + dbehf, label, comment)
                ftml.clearFeatures()
                ftml.clearBackground()
                ftml.closeTest()

            ftml.startTestGroup('All the waws')
            for uid in waws:
                c = chr(uid)
                label = 'U+{0:04X}'.format(uid)
                comment = builder.char(uid).basename
                flagUnicodeVersion((uid,))
                for featlist in builder.permuteFeatures(uids=(uid,)):
                    ftml.setFeatures(featlist)
                    ftml.addToTest(uid, c + dbehf + ' ' + zwj + c + dbehf, label, comment)
                ftml.clearFeatures()
                ftml.clearBackground()
                ftml.closeTest()

            # reh or waw plus the others
            for uid1 in (0x631, 0x648):  # (reh, waw)
                ftml.startTestGroup('{} + all the others'.format(get_ucd(uid1, 'jg')))
                c1 = chr(uid1)
                for uid2 in uids:
                    c2 = chr(uid2)
                    comment = builder.char(uid2).basename
                    label = 'U+{:04X}'.format(uid2)
                    flagUnicodeVersion((uid1,uid2))
                    for featlist in builder.permuteFeatures(uids=(uid1,uid2)):
                        ftml.setFeatures(featlist)
                        if get_ucd(uid2, 'jt') == 'D':
                            ftml.addToTest(uid2, zwj + c1 + c2 + zwj, label, comment)
                            ftml.addToTest(uid2,       c1 + c2 + zwj)
                        ftml.addToTest(    uid2, zwj + c1 + c2      , label, comment)
                        ftml.addToTest(    uid2,       c1 + c2      )
                    ftml.clearFeatures()
                    ftml.clearBackground()
                    ftml.closeTest()

        else:
            # exhaustive test for kerning data extraction
            ftml.defaultRTL = True
            addMarks = "with marks" in test.lower()
            # rules for kerning reh followed by dual- or right-joining:
            for uid1 in rehs:  # (rehs[0],)
                for uid2 in uids:
                    if uid2 == 0x0622:
                        # alefMadda gets decomposed; we'll handle this decomp below
                        continue
                    if get_ucd(uid2, 'age').startswith('13.'):
                        ftml.setBackground(ageColor)
                    for featlist in builder.permuteFeatures(uids=(uid1,uid2)):
                        ftml.setFeatures(featlist)
                        builder.render([uid1, uid2], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                        if addMarks:
                            builder.render([uid1,     uid2, ma],             ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1,     uid2, mb, ma],         ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1,     uid2, mb, mb, ma],     ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            #builder.render([uid1,     uid2, mb, mb, mb, ma], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1,     uid2, mb],             ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1,     uid2, ma, mb],         ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1,     uid2, ma, ma, mb],     ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            #builder.render([uid1,     uid2, ma, ma, ma, mb], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2],                 ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2, ma],             ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2, mb, ma],         ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2, mb, mb, ma],     ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            #builder.render([uid1, ma, uid2, mb, mb, mb, ma], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2, mb],             ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2, ma, mb],         ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, ma, uid2, ma, ma, mb],     ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            #builder.render([uid1, ma, uid2, ma, ma, ma, mb], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2],                 ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2, ma],             ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2, mb, ma],         ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2, mb, mb, ma],     ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            #builder.render([uid1, mb, uid2, mb, mb, mb, ma], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2, mb],             ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2, ma, mb],         ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2, ma, ma, mb],     ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            #builder.render([uid1, mb, uid2, ma, ma, ma, mb], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
#                            if uid2 == 0x0627:
#                                # Because alefMadda decompose for reordering we add rules for
#                                # handling *two* marks-bove between alef and mb:
#                                builder.render([uid1,     0x0627, ma, ma, mb], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
#                                builder.render([uid1, ma, 0x0627, ma, ma, mb], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
#                                builder.render([uid1, mb, 0x0627, ma, ma, mb], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                    ftml.closeTest()
                    ftml.clearFeatures()
                    ftml.clearBackground()
            # add rules for kerning followed by certain punctuation:
            for uid1 in rehs:  # (rehs[0],)
                for uid2 in filter(lambda x: x in builder.uids(), (
                        0x0021,  # EXCLAMATION MARK
                        # 0x0022,  # QUOTATION MARK
                        # 0x0028,  # LEFT PARENTHESIS
                        # 0x0029,  # RIGHT PARENTHESIS
                        # 0x002A,  # ASTERISK
                        0x002C,  # COMMA
                        # 0x002D,  # HYPHEN-MINUS
                        0x002E,  # FULL STOP
                        0x003A,  # COLON
                        0x003B,  # SEMICOLON
                        0x003F,  # QUESTION MARK
                        # 0x005B,  # LEFT SQUARE BRACKET
                        # 0x005D,  # RIGHT SQUARE BRACKET
                        # 0x007B,  # LEFT CURLY BRACKET
                        # 0x007D,  # RIGHT CURLY BRACKET
                        # 0x00A1,  # INVERTED EXCLAMATION MARK
                        # 0x00AB,  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
                        # 0x00BB,  # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
                        # 0x00BF,  # INVERTED QUESTION MARK
                        0x060C,  # ARABIC COMMA
                        0x061B,  # ARABIC SEMICOLON
                        0x061E,  # ARABIC TRIPLE DOT PUNCTUATION MARK
                        0x061F,  # ARABIC QUESTION MARK
                        # 0x066D,  # ARABIC FIVE POINTED STAR
                        # 0x06D4,  # ARABIC FULL STOP
                        0xFD3E,  # ORNATE LEFT PARENTHESIS
                        # 0xFD3F,  # ORNATE RIGHT PARENTHESIS
                        )):
                    flagUnicodeVersion((uid1,uid2))
                    for featlist in builder.permuteFeatures(uids=(uid1,uid2)):
                        ftml.setFeatures(featlist)
                        builder.render([uid1, uid2], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                        if addMarks:
                            builder.render([uid1, ma, uid2], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                            builder.render([uid1, mb, uid2], ftml, addBreaks=False, rtl=True, dualJoinMode=1)
                    ftml.clearBackground()
                    ftml.closeTest()


    if test.lower().startswith('chadian'):
        rehs = '[' + ''.join(map(chr, filter(lambda uid: get_ucd(uid, 'jg') == 'Reh', builder.uids()))) + ']'
        uids = '[' + ''.join(map(chr, filter(lambda uid: get_ucd(uid, 'jt') in ('D', 'R') or uid == 0xFD3E, builder.uids()))) + ']'
        marks = '[' + ''.join(map(chr, filter(lambda uid: get_ucd(uid, 'gc').startswith('M'), builder.uids()))) + ']'
        rehwordsRE = re.compile(f'({rehs}{marks}{uids}{marks}*)')
        with open('/SRC/ABS Text Samples/Chad/Chadian Arabic AS word list.txt', encoding="utf8") as f:
            for line_no, line in enumerate(f):
                res = ''
                matches = ''
                lastEnd = 0
                for m in rehwordsRE.finditer(line):
                    if m.start() > 0:
                        res += line[lastEnd:m.start()]
                    # I wish I could output <em> around the kerned pair, something like:
                    #     res += f'<em>{m.group()}</em>'
                    # but apparently ftml.py doesn't support this :-(
                    # So just append
                    res += m.group()
                    # Keep track af all matched strings for feature permutations
                    matches += m.group()
                    lastEnd = m.end()
                if len(res) > 0:
                    # Add tail to result
                    res += line[lastEnd:]
                    # figure features based only on what matched
                    matchedUids = list(map(ord, list(matches)))
                    flagUnicodeVersion(matchedUids)
                    for featlist in builder.permuteFeatures(uids=matchedUids):
                        ftml.setFeatures(featlist)
                        # Add to test:
                        ftml.addToTest(None,res,f'line {line_no}')
                    ftml.clearFeatures()
                    ftml.clearBackground()
                    ftml.closeTest()

    if test.lower().startswith('yehbar'):
        # Yehbarree tail interacting with diacs below previous char
        uids = sorted(filter(lambda uid: get_ucd(uid, 'jt') in ('D',), builder.uids()), key=basenameSortKey)
        markbelow = r'\u064D'  # kasratan
        markabove = r'\u06EC'  # dotStopabove-ar
        zwj = r'\u200D'   # Zero width joiner

        ftml.startTestGroup('U+06D2 yehbarree')
        yehbarree = r'\u06D2'
        for uid in uids:
            if uid < 32: continue
            c = r'\u{:04X}'.format(uid)
            label = 'U+{:04X}'.format(uid)
            comment = builder.char(uid).basename
            flagUnicodeVersion((uid,))
            for featlist in builder.permuteFeatures(uids=(uid,)):
                ftml.setFeatures(featlist)
                ftml.addToTest(uid, f"{c}{markabove}{yehbarree} {zwj}{c}{markabove}{yehbarree} {c}{markbelow}{markabove}{yehbarree} {zwj}{c}{markbelow}{markabove}{yehbarree}", label, comment)
                ftml.closeTest()
            ftml.clearFeatures()
            ftml.clearBackground()

        # Also test other forms of yehbarree (yehbarreeHamzaabove-ar, yehbarreeTwoabove, yehbarreeThreeabove-ar)
        ftml.startTestGroup('yehbarree-like')
        for yehbarree in filter(lambda x: x in builder.uids(), (0x06D3, 0x077A, 0x077B)):
            for uid in filter(lambda x: x in builder.uids(),(0x06A0, 0x08B3)):
                c = r'\u{:04X}'.format(uid)
                yb = r'\u{:04X}'.format(yehbarree)
                label = 'U+{:04X} U+{:04X}'.format(uid, yehbarree)
                comment = builder.char(uid).basename + ' ' + builder.char(yehbarree).basename
                flagUnicodeVersion((uid,yehbarree))
                for featlist in builder.permuteFeatures(uids=(uid,)):
                    ftml.setFeatures(featlist)
                    ftml.addToTest(uid, f"{c}{markabove}{yb} {zwj}{c}{markabove}{yb} {c}{markbelow}{markabove}{yb} {zwj}{c}{markbelow}{markabove}{yb}", label, comment)
                    ftml.closeTest()
                ftml.clearFeatures()
                ftml.clearBackground()

    if test.lower().startswith('feature-lang'):
        # Testing of language and feature interactions

        tests = (
            # feat, langs where it is expected to work (1) or not (0), data seq,  comment
            ('cv02', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0623,), 'Warsh alternates'),
            ('cv08', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x062C,), 'Jeem/Hah alternates'),
            ('cv12', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 0}, (0x062F,), 'Dal alternates'),
            ('cv20', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0635,), 'Sad/Dad alternates'),
            ('cv44', {'sd': 0, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0645,), 'Meem alternates'),
            ('cv48', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0647,), 'Heh alternates'),
            ('cv50', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0677,), 'U alternates'),
            ('cv60', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0622,), 'Maddah alternates'),
            ('cv62', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0651, 0x0650), 'Kasra alternates'),
            ('cv70', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x064F,), 'Damma  alternates'),
            ('cv72', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 0, 'wo': 1}, (0x064C,), 'Dammatan alternates'),
            ('cv74', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0657,), 'Inverted Damma alternates'),
            ('cv76', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0633, 0x0670), 'Superscript alef alternates'),
            ('cv78', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x0652,), 'Sukun alternates'),
            ('cv80', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x06DD,), 'Ayah alternates'),
            ('cv82', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x06F4, 0x06F6, 0x06F7, 0x0020, 0x06DD, 0x06F4, 0x06F6, 0x06F7), 'Eastern Digit alternates'),
            ('cv84', {'sd': 1, 'ur': 1, 'ku': 1, 'rhg': 1, 'wo': 1}, (0x060C,), 'Comma alternates'),
        )

        ftml._fxml.head.comment = 'In this test, the comment column indicates whether the feature is expected to ' \
                                  'function with the given language tag. '
        for (tag, expected, uids, description) in tests:
            # Skip any features that aren't in this font
            if tag not in builder.features:
                continue
            ftml.startTestGroup(f'{tag} {description}')
            featcombinations = list(builder.permuteFeatures(uids=uids))
            if len(featcombinations) == 1:
                # Hm... see if we can find this uid list in specials:
                for basename in builder.specials():
                    special = builder.special(basename)
                    if tuple(special.uids) == uids:
                        # Yes!
                        featcombinations = list(builder.permuteFeatures(feats=special.feats))
                        break
            flagUnicodeVersion(uids)
            for featlist in featcombinations:
                ftml.setFeatures(featlist)
                builder.render(uids, ftml, rtl=True, dualJoinMode=1, comment="")
            ftml.clearFeatures()
            for langID in builder.allLangs:
                ftml.setLang(langID)
                comment = ("No", "Yes")[expected.get(langID, 1)]
                for featlist in featcombinations:
                    ftml.setFeatures(featlist)
                    builder.render(uids, ftml, rtl=True, dualJoinMode=1, comment= comment if len(tuple(filter(None, featlist))) else "")
                ftml.clearFeatures()
            ftml.clearLang()
            ftml.clearBackground()


    if test.lower().startswith('classes'):
        zwj = chr(0x200D)
        lsb = '' # chr(0xF130)
        rsb = '' # chr(0xF131)

        glyphsSeen = set()

        uids = sorted(filter(lambda uid: builder.char(uid).general == 'Lo' and uid > 255, builder.uids()))
        uids = sorted(uids, key=joinGoupSortKey)
        for uid in uids:
            c = chr(uid)
            thischar = builder.char(uid)
            label = 'U+{:04X}'.format(uid)
            for featlist in builder.permuteFeatures(uids=(uid,)):
                gname = thischar.basename
                if len(featlist) == 1 and featlist[0] is not None:
                    # See if we can find an alternate glyph name:
                    feat = '{}={}'.format(featlist[0][0], featlist[0][1])
                    gname = thischar.altnames.get(feat,gname)
                if gname not in glyphsSeen:
                    glyphsSeen.add(gname)
                    comment = gname
                    ftml.setFeatures(featlist)
                    ftml.addToTest(    uid, lsb +       c       + rsb, label, comment) #isolate
                    if get_ucd(uid, 'jt') == 'D':
                        ftml.addToTest(uid, lsb +       c + zwj + rsb)  # initial
                        ftml.addToTest(uid, lsb + zwj + c + zwj + rsb)  # medial
                    if get_ucd(uid, 'jt') in ('R', 'D'):
                        ftml.addToTest(uid, lsb + zwj + c       + rsb)  # final
            ftml.clearFeatures()
            ftml.clearBackground()
            ftml.closeTest()


    ftml.writeFile(args.output)


def cmd() : execute("UFO",doit,argspec)
if __name__ == "__main__": cmd()

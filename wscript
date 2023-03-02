#!/usr/bin/python
# Smith configuration file for Scheherazade

# override the default folders
DOCDIR = ["documentation", "web"]  # add "web" to default
genout = "generated/"

# set package name
APPNAME = "ScheherazadeNew"

# set the font family name
FAMILY = APPNAME

#DEBPKG = 'fonts-sil-scheherazade'

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')
#BUILDVERSION = BUILDLABEL  # include alpha/beta

ftmlTest('tools/ftml-smith.xsl')

# APs to omit:
omitaps = '--omitaps "_above,_below,_center,_ring,_through,_aboveLeft,_H,_L,_O,_U,_R,above,below,center,ring,through,aboveLeft,H,L,O,U,R"'

# smith project-specific options:
#   --autohint - autohint the font
#   --norename - omit glyph rename step
opts = preprocess_args({'opt': '--autohint'}, {'opt': '--norename'}, {'opt': '--quick'})

cmds = [cmd('ttx -m ${DEP} -o ${TGT} ${SRC}', ['source/jstf.ttx']) ]
if '--norename' not in opts:
    cmds.append(cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/masters/${DS:FILENAME_BASE}.ufo']))
if '--autohint' in opts:
    # Note: in some fonts ttfautohint-generated hints don't maintain stroke thickness at joins; test thoroughly
    cmds.append(cmd('${TTFAUTOHINT} -n -c  -D arab -W ${DEP} ${TGT}'))

# To shrink font files for release - no longer needed?
#cmds.append(cmd('ttfsubset -s arab,latn ${DEP} ${TGT}'))

noOTkern = ' -D nokern=yes ' if '--quick' in opts else ''
noGRkern = '_nokern' if '--quick' in opts else ''

# iterate over designspace
designspace('source/ScheherazadeNew.designspace',
    instanceparams='-l ' + genout + '${DS:FILENAME_BASE}_createintance.log',
    target = process('${DS:FILENAME_BASE}.ttf', *cmds),
    ap = genout + '${DS:FILENAME_BASE}.xml',
    version=VERSION,  # Needed to ensure dev information on version string

#    graphite=gdl(genout + '${DS:FILENAME_BASE}.gdl',
#        depends=['source/graphite/master.gdl', 'source/graphite/cp1252.gdl', 'source/graphite/SchFeatures.gdh', 'source/graphite/SchGlyphs.gdh', 'source/graphite/stddef.gdh'],
#        master = 'source/graphite/master_${DS:STYLENAME}' + noGRkern + '.gdl',
#        make_params = omitaps + ' --cursive "exit=entry,rtl" --cursive "_digit=digit"',
#        params = '-d -q -e ${DS:FILENAME_BASE}_gdlerr.txt',
#        ),

    opentype = fea(genout + '${DS:FILENAME_BASE}.fea',
        mapfile = genout + "${DS:FILENAME_BASE}.map",
        master = 'source/opentype/main.feax',
        make_params = omitaps + noOTkern,
        ),
    typetuner = typetuner("source/typetuner/feat_all.xml"),
    classes = 'source/classes.xml',
    script='arab',
    pdf=fret(genout + '${DS:FILENAME_BASE}-fret.pdf', params='-r -o i -m 48'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        ),
    )

def configure(ctx):
    ctx.find_program('ttfautohint')

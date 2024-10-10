# ............... Create html based on json ............... # 
# JSON structure must be same as sample
# "styX.py"  defines the layout and arrangement of html file
# "styX.css" defines the styling of html using css


# ................... Required inputs ..................... #
# src:  source folder with all required files (json and pics)
# out:  output folder 
# json: json file name with ext
# sty:  style of html (currently only sty1 is defined)
# typ:  cv, cl, cvcl (CV or Cover Letter or combined)
# lang: de or en (for headings and hypenation)

# Imports
import os
import sys
import shutil
import importlib 
import json
import mods                          # type: ignore

# Function
def createProfile(src,out,jsFile,style,typ,lang):

    # Current directory
    cur = os.path.dirname(__file__)
    sys.path.append(cur)

    # Check source folder
    if not os.path.isdir(src):
        print('Source directory <',src,'> does not exist ...')
        print('Exiting ...')
        exit()   

    # Check output folder
    if not os.path.isdir(out):
        print('Output directory <',out,'> does not exist ...')
        print('Creating output folder ...')
        os.makedirs(out)                

    # Check JSON
    jsFile = os.path.join(src,jsFile)
    if not os.path.isfile(jsFile):
        print('JSON file <',jsFile,'> is not found ...')
        print('Exiting ...')
        exit()

    # Check style
    styCs = style+'.css'
    styPy = style+'.py'
    if not os.path.isfile(os.path.join(cur,styCs)) or not os.path.isfile(os.path.join(cur,styPy)):
        print('The style file <',style,'> is undefined ...')
        print('Selecting < sty1 > ...')
        style = 'sty1'

    # Check type
    if typ != 'cv' and typ != 'cl' and typ != 'cvcl':
        print('Content type is undefined ....')
        print('Selecting CV ...')
        typ = 'cv'

    # Check language
    if lang != 'de' and lang != 'en':
        print('Language is undefined ....')
        print('Selecting en ....')
        lang = 'en'

    # Data File
    with open(jsFile, 'r') as file:
        data = json.load(file)

    # Html
    htmlFile = os.path.join(out,'index.html')
    with open(htmlFile, 'w') as html:

        # Import style
        sty  = importlib.import_module(style)
        font = sty.getFont()
        
        # HTML header
        mods.writeHead(html,lang,styCs,font)

        # CV
        if typ == 'cv':
            # Write CV
            sty.writeCV(html,data,lang)
        # CL
        elif typ == 'cl':
            # Write CV
            sty.writeCL(html,data,lang)
        # CVCL
        elif typ == 'cvcl':
            # Write CL
            sty.writeCL(html,data,lang)
            # Write CV
            sty.writeCV(html,data,lang)

        # HTML footer
        mods.writeFoot(html)

    # Copy Style
    filename = os.path.join(cur,styCs) 
    shutil.copy2(filename,out)

    # Copy other files (except for json)
    for filename in os.listdir(src):
        # Check the file extension
        if not filename.endswith('.json'):
            shutil.copy2(os.path.join(src, filename), out)

    # Delete __pycache__
    shutil.rmtree(os.path.join(cur, '__pycache__'))



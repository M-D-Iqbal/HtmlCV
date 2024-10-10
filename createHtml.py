import sys
import os
import importlib 
import webbrowser

# Other inputs
jsFile = 'bio.json'     # json file with given template
style  = 'sty1'         # python and css style (currently only sty1 exsist)
typ    = 'cvcl'         # typ: cv, cl, or cvcl        
lang   = 'en'           # language for hyphenation and headings

# Paths (if relative then this works or define absolute paths)
curPath = os.path.dirname(__file__)
modPath = os.path.join(curPath,'CreateProfile') # Path of module
srcPath = os.path.join(curPath,'Source')        # Path of json and other sources (pic)
outPath = os.path.join(curPath,'Html')          # Output folder

# Append search path and import module
sys.path.append(modPath)
pro=importlib.import_module('createProfile')

# Build 
pro.createProfile(srcPath,outPath,jsFile,style,typ,lang)

# Open html
url = os.path.join(outPath,'index.html')
webbrowser.open(url)
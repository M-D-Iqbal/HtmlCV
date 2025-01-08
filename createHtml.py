import sys
import os
import importlib 
import webbrowser

# Other inputs
title  = 'MD-Iqbal'     # name of html without extension
style  = 'sty2'         # python and css style (currently only sty1 exsist)
typ    = 'cvcl'         # typ: cv, cl, or cvcl        
lang   = 'en'           # language for hyphenation and headings

# JSON file
if lang == 'de':
    jsFile = 'bio_de.json'
else:
    jsFile = 'bio_en.json'     

# Paths (if relative then this works or define absolute paths)
curPath = os.path.dirname(__file__)
modPath = os.path.join(curPath,'CreateProfile') # Path of module
srcPath = os.path.join(curPath,'Source')        # Path of json and other sources (pic)
outPath = os.path.join(curPath,'Html')          # Output folder

# Append search path and import module
sys.path.append(modPath)
pro=importlib.import_module('createProfile')

# Build 
pro.createProfile(title,srcPath,outPath,jsFile,style,typ,lang)

# Open html
url = os.path.join(outPath,f'{title}.html')
webbrowser.open(url)
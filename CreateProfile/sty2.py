# A sty file to write html file defined by user #
# mods function are generic #
# mods are used to place specific [section, e.g., 'work', 'eduaction'] in html
# array such as: arrWor=[["title","date"],["org"],["highlights"]] means
# ["title","date"] will be one block and ["org"],["highlights"] are seperate
# They be not be needed (or required) for all sections 

import mods # type: ignore

# Font family from fonts.googleapis
def getFont():
    # Must also be in css body: font-family: <name>, serif;
    url="https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap"
    return url

# CV
def writeCV(file,data,lang):
        
    # Page
    mods.writeEle(file,'page',2,atr='size=\"A4\"',newLine=1)
    
    # Header
    mods.writeEle(file,'div',2,atr='class=\"header\"',newLine=1)

    # Head - Left
    mods.writeEle(file,'div',2,atr='class=\"leftside\"',newLine=1)
    
    # Picture
    mods.writePic(file,data)

    # Close Head-Left
    mods.writeEle(file,'div',3)

    # Head - Right
    mods.writeEle(file,'div',2,atr='class=\"rightside\"',newLine=1)

    # Intro
    mods.writeEle(file,'div',2,atr='class=\"intro\"',newLine=1)

    # Bio
    mods.writeEle(file,'div',2,atr='class=\"bio\"',newLine=1)

    # Basics Open
    mods.writeEle(file,'div',2,atr='class=\"basics\"',newLine=1)
    # Basics
    mods.writeBasics(file,data)
    # Basics Close
    mods.writeEle(file,'div',3)

    # Close Bio
    mods.writeEle(file,'div',3)

    # Contacts
    mods.writeContact(file,data)   

    # Socials
    arrSoc=[["icon"]]
    mods.writeSocial(file,data,arrSoc)

    # Close Intro
    mods.writeEle(file,'div',3)

    # Close Head-Right
    mods.writeEle(file,'div',3)

    # Close Head
    mods.writeEle(file,'div',3)

    # Content
    mods.writeEle(file,'div',2,atr='class=\"content\"',newLine=1)

    # Profile
    heading = 1
    mods.writeProfile(file,data,heading,lang)

    # Achievements
    arrAch=[]
    mods.writeAchieve(file,data,arrAch,lang)

    # Expertise
    arrExp=[]
    mods.writeExpert(file,data,arrExp,lang)

    # Tech Skills
    arrTechSkl=[["tools"]]
    mods.writeTechSkill(file,data,arrTechSkl,lang)

    # Work
    arrWor=[["title","date"],["org"],["highlights"]]
    mods.writeWork(file,data,arrWor,lang)

    # Close Content
    mods.writeEle(file,'div',3)

    # Close Page
    mods.writeEle(file,'page',3)

    # Page
    mods.writeEle(file,'page',2,atr='size=\"A4\"',newLine=1)

    # Content without Header
    mods.writeEle(file,'div',2,atr='class=\"contentWH\"',newLine=1)

    # Education
    arrEdu=[["title","date"],["org"]]
    mods.writeEducation(file,data,arrEdu,lang)

    # Publications
    arrPub=[]
    mods.writePublic(file,data,arrPub,lang)

    # Soft Skills
    arrSoftSkl=[]
    mods.writeSoftSkill(file,data,arrSoftSkl,lang)
    
    # Languages
    arrLan=[["language"],["fluency"]]
    mods.writeLang(file,data,arrLan,lang)

    # Close Content
    mods.writeEle(file,'div',3)

    # Close Page
    mods.writeEle(file,'page',3)
 
# CL
def writeCL(file,data,lang):

    # Page
    mods.writeEle(file,'page',2,atr='size=\"A4\"',newLine=1)
    

    # Header
    mods.writeEle(file,'div',2,atr='class=\"header\"',newLine=1)

    # Head - Left
    mods.writeEle(file,'div',2,atr='class=\"leftside\"',newLine=1)
    
    # Company
    arrCom=[]
    mods.writeCompany(file,data,arrCom,lang)

    # Close Head-Left
    mods.writeEle(file,'div',3)

    # Head - Right
    mods.writeEle(file,'div',2,atr='class=\"rightside\"',newLine=1)

    # Intro
    mods.writeEle(file,'div',2,atr='class=\"intro\"',newLine=1)

    # Bio
    mods.writeEle(file,'div',2,atr='class=\"bio\"',newLine=1)

    # Basics Open
    mods.writeEle(file,'div',2,atr='class=\"basics\"',newLine=1)
    # Basics
    mods.writeBasics(file,data)
    # Basics Close
    mods.writeEle(file,'div',3)

    # Close Bio
    mods.writeEle(file,'div',3)

    # Contacts
    mods.writeContact(file,data)   

    # Socials
    arrSoc=[["icon"]]
    mods.writeSocial(file,data,arrSoc)

    # Close Intro
    mods.writeEle(file,'div',3)

    # Close Head-Right
    mods.writeEle(file,'div',3)

    # Close Head
    mods.writeEle(file,'div',3)

    # Content
    mods.writeEle(file,'div',2,atr='class=\"content\"',newLine=1)

    # Letter
    mods.writeEle(file,'div',2,atr='class=\"cl\"',newLine=1)

    # Subject
    arrSub=[]
    mods.writeSubject(file,data,arrSub,lang)

    # Letter
    arrCon=[["para"],["keyPoints"]]
    mods.writeLetCont(file,data,arrCon,lang)

    # Letter Closing
    mods.writeLetClose(file,data)
    
    # Close CL
    mods.writeEle(file,'div',3)

    # Close Content
    mods.writeEle(file,'div',3)

    # Close Page
    mods.writeEle(file,'page',3)

    
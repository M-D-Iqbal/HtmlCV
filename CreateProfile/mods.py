from datetime import datetime 
# These are the modules to add specific section in html irrespective of style 
# If new section is required create a new modules here and add that in styX.py

# -------------------------- General Mods ----------------------- #

# HTML head
def writeHead(file,lang,sty,font):

    file.write(f'<!DOCTYPE html>\n')

    file.write(f'<html lang="{lang}">\n')
    file.write(f'<head>\n')
    file.write(f'<title>index</title>\n')

    file.write(f'<link rel="stylesheet" href="{sty}"/>\n')
    file.write(f'<base target="_blank" />\n')
    file.write(f'<meta charset="UTF-8" />\n')
    file.write(f'<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n')
    file.write(f'<meta http-equiv="X-UA-Compatible" content="ie=edge" />\n')
    file.write(f'<link rel="preconnect" href="https://fonts.googleapis.com">\n')
    file.write(f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
    file.write(f'<link href="{font}" rel="stylesheet">\n')
    file.write(f'<script src="https://kit.fontawesome.com/3c80283b16.js" crossorigin="anonymous"></script>\n')
    file.write(f'</head>\n')
    file.write(f'<body>\n')

# HTML Foot
def writeFoot(file):
    file.write(f'</body>\n')
    file.write(f'</html>\n')

# HTML ELements
def writeEle(file,ele,typ,**kwargs):
    data=''
    atr=''
    newLine=False
    for key, value in kwargs.items():
        if key=='cont':
            data=value
        elif key=='atr':
            atr=value
        elif key=='newLine':
            newLine=True

    if typ==1 or typ==2:
        # open
        file.write(f'<{ele} ')
        file.write(f'{atr} ')
        file.write(f'>')
        if newLine:
            file.write(f'\n')
        # data
        if len(data)>0:
            file.write(f'{data}')
            if newLine:
                file.write(f'\n')
            # close
        if typ==1:
            file.write(f'</{ele}>\n')
    #closing
    elif typ==3:
        file.write(f'</{ele}>\n')

# Get Data
def getData(data,key):
    val=itrData(data,key)
    if val is not None:
        return val
    else:
        print('The key <',key,'> does not exist in JSON ...')
        print('This may result in missing/bad layouts ...')
        return ''
        
# Itterate over complete data
def itrData(d, key):
    if key in d:
        return d[key]
    for k, v in d.items():
        if isinstance(v, dict): 
            result = itrData(v, key)  
            if result is not None:  
                return result  
    return None  

# Section
def writeSec(file,sec,head,clss,arrange):
    # Main 
    mainAtr='class="'+clss+'"'
    writeEle(file,'div',2,atr=mainAtr,newLine=1)
    # Heading
    if len(head) != 0:
        writeEle(file,'div',1,atr="class=\"head\"",cont=head)
    # Dataset
    for i in range(len(sec)):
        lvl=1
        curSec=sec[i]
        writeEle(file,'div',2,atr="class=\"item\"",newLine=1)
        # Arrangements
        if len(arrange)==0:
            file.write(f'{curSec}\n')
        else: 
            for key in arrange:
                if len(key)>1:
                    lvl=+lvl
                    lvlKey='class="line-'+str(lvl)+'"'
                    # open lvl
                    writeEle(file,'div',2,atr=lvlKey,newLine=1)
                    for j in range(len(key)):
                        if key[j] in curSec:
                            val=curSec[key[j]]
                            valAtr='class="'+key[j]+'"'
                            writeEle(file,'span',1,atr=valAtr,cont=val)
                    # Closing lvl        
                    writeEle(file,'div',3)
                elif len(key)==1:
                    if key[0] in curSec:
                        valAtr='class="'+key[0]+'"'
                        val=curSec[key[0]]
                        if isinstance(val, str):
                            writeEle(file,'div',1,atr=valAtr,cont=val)
                        else:
                            writeEle(file,'div',2,atr=valAtr,newLine=1)
                            writeEle(file,'ul',2,newLine=1)
                            for k in val:
                                writeEle(file,'li',1,cont=k)  			
                            writeEle(file,'ul',3)
                            writeEle(file,'div',3)
        # Closing item
        writeEle(file,'div',3)
    # Closing Main
    writeEle(file,'div',3)

# -------------------------- Content Mods ----------------------- #    
# Profile Pic
def writePic(file,data):
    basics=getData(data,'basics')
    pic=getData(basics,'proPic')
    atr='class="profilePic" src="'+pic+'"'
    writeEle(file,'img',1,atr=atr)

# Name and label
def writeBasics(file,data):
    basics=getData(data,'basics')
    first=getData(basics,'first')
    last=getData(basics,'last')
    label=getData(basics,'label')
    writeEle(file,'div',2,atr="class=\"name\"",newLine=1)
    writeEle(file,'span',1,atr="class=\"first\"",cont=first)
    writeEle(file,'span',1,atr="class=\"last\"",cont=last)
    writeEle(file,'div',3)
    writeEle(file,'div',1,atr="class=\"label\"",cont=label)

# Summary
def writeSummary(file,data):
    basics=getData(data,'basics')
    summary=getData(basics,'summary')
    writeEle(file,'div',1,atr="class=\"summary\"",cont=summary)

# Contact
def writeContact(file,data):
    basics=getData(data,'basics')
    email=getData(basics,'email')
    phone=getData(basics,'phone')
    locat=getData(basics,'address')
    atrEm='href="mailto:'+email+'"'
    # Contact
    writeEle(file,'div',2,atr="class=\"contact\"",newLine=1)
    # Email
    writeEle(file,'div',2,atr="class=\"item\"",newLine=1)
    writeEle(file,'i',1,atr="class=\"fa-solid fa-envelope\" aria-hidden=\"true\"")
    writeEle(file,'a',1,atr=atrEm,cont=email)
    writeEle(file,'div',3)
    # Phone
    writeEle(file,'div',2,atr="class=\"item\"",newLine=1)
    writeEle(file,'i',1,atr="class=\"fa-solid fa-phone\" aria-hidden=\"true\"")
    file.write(f'{phone}\n')
    writeEle(file,'div',3)
    # Address
    writeEle(file,'div',2,atr="class=\"item\"",newLine=1)
    writeEle(file,'i',1,atr="class=\"fa-solid fa-map-marker\" aria-hidden=\"true\"")
    file.write(f'{locat}\n')
    writeEle(file,'div',3)
    # Close contact
    writeEle(file,'div',3)

# Keywords
def writeKeywords(file,data,array,lang): 
    # Heading
    head = ''
    # Class
    clss = 'Key'
    # Data
    sec=getData(data,'keywords')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Education
def writeEducation(file,data,array,lang): 
    # Heading
    if lang == 'de':
        head = 'Studium'
    else:
        head = 'Education'
    # Class
    clss = 'Edu'
    # Data
    sec=getData(data,'education')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Work
def writeWork(file,data,array,lang): 
    # Heading
    if lang == 'de':
        head = 'Berufserfahrung'
    else:
        head = 'Work Experience'
    # Class
    clss = 'Wor'
    # Data
    sec=getData(data,'work')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Expertise
def writeExpert(file,data,array,lang): 
    # Heading
    if lang == 'de':
        head = 'Fachkenntnisse'
    else:
        head = 'Expertise'
    # Class
    clss = 'Exp'
    # Data
    sec=getData(data,'expertise')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Skills
def writeSkill(file,data,array,lang): 
    # Heading
    if lang == 'de':
        head = 'F&#228higkeiten'
    else:
        head = 'Skills'
    # Class
    clss = 'Ski'
    # Data
    sec=getData(data,'skills')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Languages
def writeLang(file,data,array,lang): 
    # Heading
    if lang == 'de':
        head = 'Sprachen'
    else:
        head = 'Languages'
    # Class
    clss = 'Lan'
    # Data
    sec=getData(data,'languages')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Publications
def writePublic(file,data,array,lang): 
    # Heading
    if lang == 'de':
        head = 'Publikationen'
    else:
        head = 'Publications'
    # Class
    clss = 'Pub'
    # Data
    sec=getData(data,'publications')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Company
def writeCompany(file,data,array,lang):
    # Heading
    head = ''
    # Class
    clss = 'Company'
    # Data
    sec=getData(data,'company')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Subject
def writeSubject(file,data,array,lang):
    # Heading
    head = ''
    # Class
    clss = 'Subject'
    # Data
    sec=getData(data,'subject')
    # Write Data
    writeSec(file,sec,head,clss,array)

# Content
def writeLetCont(file,data,array,lang):
    # Heading
    head = ''
    # Class
    clss = 'Let-cont'
    # Data
    sec=getData(data,'content')
    # Write Data
    writeSec(file,sec,head,clss,array)
        
# Letter Closing
def writeLetClose(file,data):
    basics=getData(data,'basics')
    name=getData(basics,'first')+' '+getData(basics,'last')
    sign=getData(basics,'sign')
    city=getData(basics,'city')
    day=datetime.now().day
    month=datetime.now().month
    year=datetime.now().year
    date=str(day)+'.'+str(month)+'.'+str(year)
    # Close
    writeEle(file,'div',2,atr='class=\"Close-let\"',newLine=1)
    writeEle(file,'div',2,atr='class=\"NameCityDate\"',newLine=1)
    writeEle(file,'div',1,atr='class=\"Let-name\"',cont=name,newLine=1)
    writeEle(file,'div',2,atr='class=\"Let-cityDate\"',newLine=1)
    writeEle(file,'span',1,atr='class=\"Let-city\"',cont=city)
    writeEle(file,'span',1,atr='class=\"Let-date\"',cont=date)
    writeEle(file,'div',3)
    writeEle(file,'div',3)
    writeEle(file,'div',2,atr='class=\"sign\"',newLine=1)
    if sign != '':
        signAtr='class="SignPic" src="'+sign+'"'
        writeEle(file,'img',1,atr=signAtr)
    writeEle(file,'div',3)
    writeEle(file,'div',3)

# Socials
def writeSocial(file,data,arrange):
    soc=getData(data,'socials')
    mainAtr='class=\"Social\"'
    writeEle(file,'div',2,atr=mainAtr,newLine=1)
    for i in range(len(soc)):
        writeEle(file,'div',2,atr="class=\"item\"",newLine=1)
        atr='href="'+soc[i]["url"]+'"'
        if arrange[0][0] == 'name':
            writeEle(file,'a',1,atr=atr,cont=soc[i]["name"])
        else: 
            writeEle(file,'a',2,atr=atr,newLine=1)
            atrIc='class="'+soc[i]["icon"]+'" aria-hidden="true"'
            writeEle(file,'i',1,atr=atrIc)
            writeEle(file,'a',3)
        writeEle(file,'div',3)
    writeEle(file,'div',3)    


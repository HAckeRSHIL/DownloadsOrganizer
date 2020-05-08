# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:58:00 2020

@author: HAckeRSHIL
LinkedIn: HAckeRSHIL
Instagram : HAckeRSHIL
Twitter : HAckeRSHIL
GitHub : HAckeRSHIL
"""

import os
import shutil
# Dictonary to find the files generalized class by its extention YOU can edit this too according to your preferance
classifier={
        "Data":['csv','dat','ged','key','keychain','sdf','xml','vcf'],
        "Documents" : ['pdf','doc','docx','log','msg','odt','pages','rtf','tex','txt','wpd','wps','ods','ppt','pptx'],
        "Audio":['aif','iif','m3u','m4a','mid','mp3','mpa','wav','wma'],
        "Video":['avi','flv','m4v','mov','mp4','mpg','rm','srt','swf','vob','wmv','asf','3g2','3gp'],
        "Images":['bmp','dds','gif','heic','jpg','png','psd','pspimage','tga','thm','tif','tiff','yuv','ai','eps','svg'],
        "Database":['accdb','db','dbf','mdb','pdb','sql'],
        "Executable":['apk','app','bat','cgi','com','exe','gadget','jar','wsf'],
        "Web files":['asp','aspx','css','html','htm','cer','cfm','csr','dcr','js','jsp','php','rss','xhtml'],
        "Compressed":['zip','7z','rar','rpm','sitx','zipx','tar','tar.gz','gz','pkg','deb','cbr'],
        "Developer files" : ['c','class','cpp','cs','dtd','fla','h','java','lua','m','pl','py','sh','sln','swift','vb','vcxproj','ipynb'],
        "Torrent":['torrent']
        }

#This function take extention as input and return the generalized class using classifier dict
def getclass(extention):
    for key,value in classifier.items() :
        if extention in value:
            return str(key)
    #if extention not found then add that in others
    return "Others"

#Creating all the class which are in classfier's keys and others
#If there is already a dictonary named as the key then do nothing 
def createfolders():
    for key in classifier.keys():
        try:
            os.mkdir(path+'\\'+key)
        except FileExistsError:
            continue
    try:
        os.mkdir(path+'\\others')
    except FileExistsError:
        print('Do nothing lol')
    
        
#scan through all the file which is in current directory finding its extention and moving to certain dictonary according to that
def classify():
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
        # Only process the entries which are files
          if entry.is_file():
            #finding extention through filename
            extention = os.path.splitext(entry.name)[1][1:]
            #calling the getclass function which return its generalized form name (dictonary)
            classfolder = getclass(extention)
            #src = current path of file
            #des = where should it go (MAKE SURE THAT YOU ALREADY HAVE FOLDERS to go through in path)
            src=path+'\\'+entry.name
            des=path+'\\'+classfolder+'\\'+entry.name
            #print(src+'--->'+des)
            #shutil.copy for copy and shutil.move to move
            shutil.move(src,des)
            

# detect the current working directory
path = os.getcwd()
#Create folders first in that directories (all keys of classifier)
createfolders()
#Classify them according to their extention
classify()
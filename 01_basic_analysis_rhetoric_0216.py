from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import os
import re
import codecs
import nltk
from nltk.tokenize import word_tokenize

#pc
#os.chdir("C:\Users\ps22344.AUSTIN\Desktop")
#mac
os.chdir("/Users/ps22344/Desktop")

#wheres the files?
dir="final_files"
filis=os.listdir(dir)


#setting up some functions
def tagextractor(text, tag, fili):
    regexstring="<"+tag+"=(.*?)>"
    result=re.findall(regexstring, text, re.DOTALL)
    if len(result) != 1:
        print "alarm in tagextractor", fili, result
    return result[0]
    
def textextractor(text, fili):
    regexstring="<text>(.*?)</text>"
    result=re.findall(regexstring, text, re.DOTALL)
    if len(result) != 1:
        print "alarm in adtextextractor", fili, result
    return result[0]

def wordfinder(word, text, fili):
	regexstring=word
	result=re.findall(regexstring, text)
	print result
    
    
#nltk.download()    




print filis

for fili in filis:
	print "\n---------------\n"
	inputi=codecs.open(os.path.join(dir,fili), "r", "utf-8").read()
	text=textextractor(inputi, fili)
	wordcount=len(word_tokenize(text))
	print fili
	print "character length", len(inputi)
	print "word count", wordcount
	ethos=wordfinder("ethos", text, fili)
	#print word_tokenize(text)[:3]
	
	
	
	

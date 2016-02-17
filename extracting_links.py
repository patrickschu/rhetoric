## getting some loebs
print "start"
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import os
import re
import codecs
import nltk
import urllib
#pc
#os.chdir("C:\Users\ps22344.AUSTIN\Desktop")
#mac
os.chdir("/Users/ps22344/Desktop")

#some functions

def linkextracter (urllibobject):
	soup=BeautifulSoup(urllibobject, "html.parser")
	print soup.prettify()
 	fulllinks=[i['href'] for i in soup.find_all('a')]
	print fulllinks
 	


arislink=urllib.urlopen("http://www.google.com/").read()
linkextracter(arislink)


# http://www.loebclassics.com/browse?t1=author.aris

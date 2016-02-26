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
	fulllinks=[i['href'] for i in soup.find_all('a')]
 	#print fulllinks
 	return fulllinks
 	
def bookdownloader(base, urllibobject, filetype):
	soup=BeautifulSoup(urllibobject, "html.parser")
	#this we find under CSS selectors in the doc
	#if we feel adventurous, we can use the select thing above as well
	#but let's not change winning team
	#somewhat winning, that is
	fulllinks=soup.select('a[href]')
	downloadlinks=[d['href'] for d in fulllinks if filetype in d['href']]
	print "downloadlinks found: ", len(downloadlinks)
	for downi in downloadlinks:
		print "downloading", downi
		urllib.urlretrieve("/".join([base,downi]), "_".join([base.lstrip(baselink),downi]))

	
	
#of urls, use "/".join(), dumbass	 	

#basic things
baselink="http://classics.mit.edu/"

classiclink=urllib.urlopen(baselink+"Browse/index.html").read()
results=linkextracter(classiclink)
#print results

authorlinks =[i for i in results if "browse" in i]
# authorlinks= [u'browse-Aeschines.html', u'browse-Aeschylus.html', u'browse-Aesop.html', u'browse-Andocides.html', u'browse-Antiphon.html', u'browse-Apollodorus.html', u'browse-Apollonius.html', u'browse-Apuleius.html', u'browse-Aristophanes.html', u'browse-Aristotle.html', u'browse-Antoninus.html', u'browse-Augustus.html', u'browse-Bacchylides.html', u'browse-Caesar.html', u'browse-Cicero.html', u'browse-Demades.html', u'browse-Demosthenes.html', u'browse-Dinarchus.html', u'browse-Diodorus.html', u'browse-Epictetus.html', u'browse-Epicurus.html', u'browse-Euclid.html', u'browse-Euripides.html', u'browse-Galen.html', u'browse-Herodotus.html', u'browse-Hesiod.html', u'browse-Hippocrates.html', u'browse-Hirtius.html', u'browse-Homer.html', u'browse-Horace.html', u'browse-Hyperides.html', u'browse-Isaeus.html', u'browse-Isocrates.html', u'browse-Josephus.html', u'browse-Livy.html', u'browse-Lucan.html', u'browse-Carus.html', u'browse-Lycurgus.html', u'browse-Lysias.html', u'browse-Ovid.html', u'browse-Pausanias.html', u'browse-Pindar.html', u'browse-Plato.html', u'browse-Plotinus.html', u'browse-Plutarch.html', u'browse-Porphyry.html', u'browse-Quintus.html', u'browse-Sophocles.html', u'browse-Strabo.html', u'browse-Tacitus.html', u'browse-Thucydides.html', u'browse-Virgil.html', u'browse-Xenophon.html', u'browse-Confucius.html', u'browse-Lao.html', u'browse-Tzu.html', u'browse-Ferdowsi.html', u'browse-Khayyam.html', u'browse-Sadi.html']
# authorlinks= [u'browse-Aristotle.html']


#for each author, we find the books listed
for author in authorlinks:
	authorname=author.lstrip("browse-").rstrip(".html")
	print "\n\n\n\n working on ", author
	print str(baselink+authorname)
	books=urllib.urlopen(baselink+"/Browse/"+author).read()
	result=linkextracter(books)
	#stolen from: http://stackoverflow.com/questions/11740814/is-there-a-way-to-use-two-if-conditions-in-list-comprehensions-in-python
	booklinks=[b for b in result if  all (excluder not in b.lower() for excluder in ['buy', 'help', 'index'])]
	print "found the following books"
	for booki in booklinks:
		print booki
		downloadlink=baselink+booki.lstrip("/")
		print downloadlink
 		bookdownloader(baselink+authorname, urllib.urlopen(downloadlink).read(), "txt")
		break
# 		#print str(baselink+author.lstrip("browse-").rstrip(".html")+booki)

print "finished"

#print authorlinks

# http://www.loebclassics.com/browse?t1=author.aris
#index, buy and help are evil

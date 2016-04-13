
# check out formatting
# <file> <title=rhetoric> <author=aristotle> <translator=freese, j> 
# <source=http://www.perseus.tufts.edu/> <pubdate=1926> <bibinfo=Aristotle in 23 Volumes, ... <text> 
# blablabla </text> </file>

import os, codecs, re

print "start"

#set up
signal="\n----------------------------------------------------------------------\n"
good=[]

print os.getcwd()
files=[i for i in os.listdir("classics_0325") if not i.startswith(".")]

print "We have {} files".format(len(files))

files_to_process=[i for i in files if not open (
		"classics_0325/"+i, "r").read().startswith("<file")]
		
print "We need to process {} of them".format(len(files_to_process))

print files_to_process

for fili in files_to_process:
	print fili
	inputfile=open(os.path.join("classics_0325", fili), "r").read()
	author = fili.split("_")[0]
	title= fili.split("_")[1]
	title=re.sub("(1?b?\.mb\.txt|1?b?\.pl\.txt)", "", title)
	#delete
	# if inputfile.startswith("<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">"):
# 		os.remove(os.path.join("classics_0325", fili))
# 		print fili, "removed"
	#print title
	#print inputfile.split(" ")[:30]
	text=re.findall(signal+"(.*?)"+signal, inputfile, re.DOTALL)
	print len(text)
	#this loop takes care of the ones that work easily
	if len(text) == 1:
		text=text
	#if we dont find anythin with the regex, here we go
	# the end is still the signal one would hope
	if len(text) == 0:
		start="Available online at\n    http://classics.mit.edu/.*?html"
		text=re.findall(start+"(.*?)"+signal, inputfile, re.DOTALL)
	# for length btw 2 and 6
	if len(text)  < 8 and len(text) > 1:
		start="Available online at\n    http://classics.mit.edu/.*?html"
		end="----------------------------------------------------------------------\n\nCopyright statement"
		text=re.findall(start+"(.*?)"+end, inputfile, re.DOTALL)
	if len(text) != 1:
		print "ALARM", fili, len(text)
 	text=text[0]
 	outputfile=open(os.path.join("classics_0413", fili), "w")
	outputfile.write(
		"<file> <title="+title+
		"> <author="+author+
		"> <translator= > <source= > <pubdate= > <bibinfo= > <text> "+
		text+
		" </text> </file>"
		)
	outputfile.close() 
	print fili, "processed", outputfile, "\n\n---\n"
# blablabla </text> </file>
# 		#print fili
# 		if len(text) != 1:
# 			print fili
# 		#print text[0]
# 		#print inputfile[:200]
	# if len(text) == 4:
# 		start="Available online at\n    http://classics.mit.edu/.*?html"
#  		text=re.findall(start+"(.*?)"+signal, inputfile, re.DOTALL)
#  	if len(text) ==5 :
#  		start="Available online at\n    http://classics.mit.edu/.*?html"
#  		text=re.findall(start+"(.*?)"+signal, inputfile, re.DOTALL)
#  		if len(text) == 0:
#  			print fili
# 			print len(text)
# 			print inputfile[:200]
# 			
# 	if len(text) ==6 :
#  		start="Available online at\n    http://classics.mit.edu/.*?html"
#  		text=re.findall(start+"(.*?)"+signal, inputfile, re.DOTALL)
#  		if len(text) == 0:
#  			print fili
# 			print len(text)
# 			print inputfile[:200]
# 	if len(text) != 1:
# 		print "ALARM"
# 		print fili, len(text), "\n\n------\n\n\n"			

print "finish"

	
	

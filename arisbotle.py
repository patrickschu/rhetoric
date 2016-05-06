#!/usr/bin/env python

import re, numpy as np, codecs, os, nltk, collections, time
from string  import digits, punctuation
import generatortools as gt
import sys

def main(input_folder, iter = 1000, probability_cutoff = - 35 , threshold = 10, tweet=True):
	"""
	iter sets the number of times to run the sentence builder
	threshold is fed into the sentbuilder and sets the number of items to consider when choosing from the candidates
	for next word from a sorted list.
	probability_cutoff sets the lowest probability (log) of a sentence to be published
	"""
	
	success=0
	tweets=[]
	outputfile=codecs.open("aristotlelog_"+time.strftime("%m_%d_%Y")+".txt",  "a", "utf-8")
	dir=input_folder
	files=[os.path.join("out", i) for i in os.listdir(dir) if not i.startswith(".")]
	#print "We're working with these files: ", files
	print "Making the word dicti"
	worddicti=gt.dictmaker(files, 1)
	print "We have {} unique words and {} words total".format(len(worddicti.keys()), sum(worddicti.values()))
	print "Making the bigram dicti"
	bigramdicti=gt.dictmaker(files, 2)
	print "Making the trigram dicti"
	trigramdicti=gt.dictmaker(files, 3)
	for item in range(0,int(iter)):
		print "Starting the sentence builder"
		sent, probs = gt.sentbuilder(".", ".?!", threshold, worddicti,  bigramdicti, trigramdicti)
		#here we set the probability cutoff (logged values)
		#note that we might want to exclude the first, "seed" item
		
		if sum(probs[1:len(probs)]) > int(probability_cutoff):
				output=" ".join(sent).lstrip(".")
				print "Aristotle says: "
				print output, "\n"
				print "Probability", sum(probs[1:len(probs)]), probs
				success=success+1
				tweets.append(output)
				if tweet == True:
					bot=gt.loginmachine("twitter_keys.txt")
					bot.update_status(status=tweets[success-1])
					print "tweeting"
					time.sleep(500)
					print "now sleeping"
		else:
				print "No good sentence found"
				outputfile.write (" ".join(sent)+","+str(sum(probs[1:len(probs)]))+","+" ".join([str(i) for i in probs])+"\n")
				
	print "{} successes".format(success)
	outputfile.close()		

if __name__ == "__main__":
	main(*sys.argv[1:])

import re, numpy as np, codecs, os, nltk, collections, time
from string  import digits, punctuation
import generatortools as gt
		

##need to use word dict counts instead of overall-count for trigrams, right???
## <s> and </s>
## use bigram probs for evaluation
# i.e. is a problem


def main(input_folder, iter = 100, threshold = 5, probability_cutoff = - 20):
	"""
	iter sets the number of times to run the sentence builder
	threshold is fed into the sentbuilder and sets the number of items to consider when choosing from the candidates
	for next word from a sorted list.
	probability_cutoff sets the lowest probability (log) of a sentence to be published
	"""
	
	output=open("aristotlelog_"+time.strftime("%m_%d_%Y")+".txt", "a")
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
	print "Starting the sentence builder"
	for item in range(0,iter):
		sent, probs = gt.sentbuilder(".", ".?!", threshold, worddicti,  bigramdicti, trigramdicti)
		#here we set the probability cutoff (logged values)
		if sum(probs) > probability_cutoff:
				out=" ".join(sent).lstrip(".")
				print "Aristotle says: "
				print out, "\n"
				print "Probability", sum(probs), probs
		else:
				print "No good sentence found"
				output.write (" ".join(sent)+","+sum(probs)+","+" ".join(probs))
				output.close()
				

main("out")
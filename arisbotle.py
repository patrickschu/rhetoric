#!/usr/bin/env python

import re, numpy as np, codecs, os, nltk, collections, time
from string  import digits, punctuation
import generatortools as gt
import sys
		

##need to use word dict counts instead of overall-count for trigrams, right???
## <s> and </s>
## use bigram probs for evaluation
# i.e. is a problem
# make the threshold for random selection variable, i.e. top X percent, so it won't break
# log probabilities from the start
# cutoff probability could be relative to sentence lenght, too
# 
# import schedule
# import time
# 
# def job():
#     print("I'm working...")
# 
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# 
# while 1:
#     schedule.run_pending()
#     time.sleep(1)


def tweeter(interval, input_list):
		for i in range(0,5):
			time.sleep(interval)
			if len (input_list) > 0:
				bot=gt.loginmachine("twitter_keys.txt")
				bot.update_status(status=tweets[success-1])
				print "tweeting"
			else:
				pass

def main(input_folder, iter = 1000, probability_cutoff = - 40 , threshold = 10, tweet=True):
	"""
	iter sets the number of times to run the sentence builder
	threshold is fed into the sentbuilder and sets the number of items to consider when choosing from the candidates
	for next word from a sorted list.
	probability_cutoff sets the lowest probability (log) of a sentence to be published
	"""
	
	success=0
	tweets=[]
	outputfile=open("aristotlelog_"+time.strftime("%m_%d_%Y")+".txt", "a")
	dir=sys.argv[1]
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
		#note that we might want to exclude the first, "seed" item
		if sum(probs) > probability_cutoff:
				output=" ".join(sent).lstrip(".")
				print "Aristotle says: "
				print output, "\n"
				print "Probability", sum(probs), probs
				success=success+1
				tweets.append(output)
				if tweet == True:
					bot=gt.loginmachine("twitter_keys.txt")
					bot.update_status(status=tweets[success-1])
					print "tweeting"
		else:
				print "No good sentence found"
				outputfile.write (" ".join(sent)+","+str(sum(probs))+","+" ".join([str(i) for i in probs])+"\n")
				
	print "{} successes".format(success)
	outputfile.close()		

if __name__ == "__main__":
	main(sys.argv[1:])
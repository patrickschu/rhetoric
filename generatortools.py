import re
import nltk
import collections
import codecs
import random
import math
from twython import Twython





def dictmaker(filelist, no_of_grams=1, lowercase_text=False, rm_punct=False, rm_allcaps=True, rm_quotes=True, rm_minor_punct=True):
	
	''' 
	Input: a list of .txt file paths. Finds text within <text> ... </text>. 
	Returns dictionary of ngram counts, default setting is unigrams. 
	Format: dict {ngram 1:count, ngram 2: count, ...}
	'''
	
	vocab=collections.defaultdict(int)
	#we should eliminate all caps words as these are section headers
	for fili in filelist:
		inputfile=codecs.open(fili, "r", "utf-8").read()
 		inputtext=adtextextractor(inputfile, fili)
 		splittext=nltk.word_tokenize(inputtext)
 		cleantext=splittext
 		if rm_allcaps == True:
 			#this removes words in all caps
			cleantext=[i for i in cleantext if not i.isupper()]
		if lowercase_text == True: 
			# lower case all words
			cleantext=[i.lower() for i in cleantext]
		if rm_punct==True:
			#removes punctuation as item and if adhering to word items
			#maybe we want to separate these out later
			cleantext=[i.strip(punctuation) for i in cleantext if re.search("\w+", i)]
		if rm_quotes==True:
			cleantext=[i.strip("\"\'") for i in cleantext]
		if rm_minor_punct==True:
			cleantext=[i for i in cleantext if i not in [",", ";","-", "(", ")"]]
		ngrams=find_ngrams(cleantext,no_of_grams)
		for ngram in ngrams:
			if len(ngram) == 1:
				vocab[ngram[0]]=vocab[ngram[0]]+1
			else:		
				vocab[ngram]=vocab[ngram]+1
	return vocab


#this is only called on within sentbuilder
def generatemachine(worddict, ngramdict, string):

	'''
	This takes a vocab dictionary and a ngram dictionary to compute probabilities 
	(relative freqs) for the "string" input. Returns a dictionary of frequencies. 
	'''

	# establishing the n of our ngrams
	gramlength=set([len(i) for i in ngramdict.keys()])
	indexer=list(gramlength)[0]-1
	#dict to collocation counts for the string
	string_dict=collections.defaultdict(float)
	# dict to compute frequencies
	freq_dict=collections.defaultdict(float)
	#iterating over ngrams in the input dict
	for ngram in ngramdict:
		#remember that string is our variable
		if string in ngram:
			#exclude if last in gram
			if len(ngram) <= ngram.index(string)+indexer:
				#string_dict['skipped']=string_dict['skipped']+ngramdict[ngram]
				pass
			else:
				following_word=ngram[ngram.index(string)+indexer]
				string_dict[following_word]=string_dict[following_word]+ngramdict[ngram]
	# calculating relative frequencies
 	for entry in string_dict:
 		if not entry =='Part':
 			freq_dict[entry]=string_dict[entry]/worddict[string]
 	return freq_dict
 

def sentbuilder(startstring, endstring, threshold, worddict, *args):
	
	'''
	Takes a string to start and a string to end the sentence, generates sentences. 
	Worddict needs to be overall vocab, then unlimited number of ngram dictionaries as args.
	Threshold sets the number of items to consider when choosing from the candidates
	for next word from sorted list. 
	***Not yet flexible to go over trigram / random number.
	***	
	'''
	#start with ".", pick follow up from list of top fifty, until you hit "." again
	sentence=[startstring]
	probs=[]
	#total word count
	total=sum(worddict.values())
	first_word=generatemachine(worddict, args[0], startstring)#random.choice(generatemachine(worddict, arg[0], "."))
	first_word_sorted=sorted(first_word.items(), key=lambda x: x[1], reverse=True)
	word=random.choice(first_word_sorted)
	#print word
	sentence.append(word[0])
	probs.append(math.log(word[1]))
 	while word[0] not in endstring and len(sentence) < 8:
 		prev_word=sentence[len(sentence)-2]
 		#print prev_word
 		current_word=sentence[len(sentence)-1]
 		#print current_word
 		word_less_two=generatemachine(worddict, args[1],  prev_word)
 		#print "word less 2 length ", len(word_less_two)
 		word_less_one=generatemachine(worddict, args[0], current_word)
 		#print "word less 1 length ", len(word_less_one)
 		freqs={k:v*word_less_two.get(k, 1) for k, v in word_less_one.items()}
 		#print "word less 2 UPDATED length ", len(word_less_two)
 		next_word_sorted=sorted(freqs.items(), key=lambda x: x[1], reverse=True)
 		#word=next_word_sorted[0][0]
 		word=random.choice(next_word_sorted[:int(threshold)])
 		sentence.append(word[0])
 		probs.append(math.log(word[1]))
 	else:
 		return (sentence, probs)

def loginmachine(filename):
	'''takes file with login data formatted like so:
	API_key,API_secret,App_token,App_secret
	logs in, returns Twython object'''
	keyfile=open(filename, "r")
	login=keyfile.read()
	key=login.split(",")[0]
	secret=login.split(",")[1]
	token=login.split(",")[2]
	token_secret=login.split(",")[3]
	twython_object = Twython(key, secret,token,token_secret)
	return twython_object

#helper functions

def adtextextractor(text, fili):
    regexstring="<text>(.*?)</text>"
    result=re.findall(regexstring, text, re.DOTALL)
    if len(result) != 1:
        print "alarm in adtextextractor", fili, result
    return result[0]


#source: http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
def find_ngrams(text, n):
  return zip(*[text[i:] for i in range(n)])
  
  

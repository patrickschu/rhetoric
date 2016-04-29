import re
import nltk
import collections
import codecs





def dictmaker(filelist, no_of_grams=1, lowercase_text=False, remove_punct=False, remove_allcaps=True, remove_quotes=True):
	
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
 		if remove_allcaps == True:
 			#this removes words in all caps
			cleantext=[i for i in cleantext if not i.isupper()]
		if lowercase_text == True: 
			# lower case all words
			cleantext=[i.lower() for i in cleantext]
		if remove_punct==True:
			#removes punctuation as item and if adhering to word items
			#maybe we want to separate these out later
			cleantext=[i.strip(punctuation) for i in cleantext if re.search("\w+", i)]
		if remove_quotes==True:
			cleantext=[i.strip("\"\'") for i in cleantext]
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

	gramlength=set([len(i) for i in ngramdict.keys()])
	indexer=list(gramlength)[0]-1
	#output: "." + n*x + "."
	string_dict=collections.defaultdict(float)
	freq_dict=collections.defaultdict(float)
	for ngram in ngramdict:
		#remember that string is our variable
		if string in ngram:
			#string_dict['overall_count']=string_dict['overall_count'] + ngramdict[ngram]
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
  
  

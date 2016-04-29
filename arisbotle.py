import re, numpy as np, codecs, os, nltk, collections, random, math
from string  import digits, punctuation
import generatortools as gt


#this is only called on within sentbuilder
def generatemachine( worddict, ngramdict, string):
	count=0
	#output: "." + n*x + "."
	string_dict=collections.defaultdict(float)
	freq_dict=collections.defaultdict(float)
	
	for ngram in ngramdict:
		#remember that string is our variable
		if string in ngram:
			#exclude if last in gram
			if len(ngram) == ngram.index(string)+1:
 				pass
			else:
				following_word=ngram[ngram.index(string)+1]
				string_dict[following_word]=string_dict[following_word]+1

	
 	# calculating relative frequencies
 	for entry in string_dict:
 		if not entry == 'overall_count' and not entry =='Part':
 			freq_dict[entry]=(string_dict[entry]/worddict[tuple(string)])
	freq_dict_sorted=sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
 	print freq_dict_sorted
	return freq_dict_sorted
##need to use word dict counts instead of overall-count for trigrams, right???
## <s> and </s>
## use bigram probs for evaluation



dir="out"
files=[os.path.join("out", i) for i in os.listdir(dir) if not i.startswith(".")]
worddicti=gt.dictmaker(files, 1)
gramdicti=gt.dictmaker(files, 3)
generatemachine(worddicti, gramdicti, ".")



# 	#stolen from: http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

import re, numpy as np, codecs, os, nltk, collections, random, math
from string  import digits

print "start"
#helper funcs
t=0
def adtextextractor(text, fili):
    regexstring="<text>(.*?)</text>"
    result=re.findall(regexstring, text, re.DOTALL)
    if len(result) != 1:
        print "alarm in adtextextractor", fili, result
    return result[0]

#stole this from: http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
def find_ngrams(text, n):
  return zip(*[text[i:] for i in range(n)])

#collect dictionary of trigrams

#
###BUILDING VOCAB
#
#threshold sets how many times a word needs to occur to be included in the featuredict
def dictmaker(filelist, no_of_grams=2):
	#this is our general vocab
	vocab=collections.defaultdict(int)
	#collecting words
	#we should eliminate all caps words as these are section headers
	for fili in filelist:
		inputfile=codecs.open(os.path.join("out",fili), "r", "utf-8").read()
 		inputtext=adtextextractor(inputfile, fili)
 		splittext=nltk.word_tokenize(inputtext)
		cleantext=[i for i in splittext if not i.isupper()]
		#cleanertext=[i for i in cleantext if not i in digits]
		ngrams=find_ngrams(cleantext,no_of_grams)
		for ngram in ngrams:
			vocab[ngram]=vocab[ngram]+1
	return vocab
		#cleantext_lo=[i.lower() for i in cleantext]
		
# 			splittextlo=[i.lower() for i in splittext]



#calculate probs
# we 
# generate random sentence from word dict
# calculate gram probability
# we generate:
# "i have"
# probability of -. followed by i - i followed by have -have followed by .


#this is only called on within sentbuilder
def generatemachine(gramdict,worddict, string):
	count=0
	#output: "." + n*x + "."
	temp_dict=collections.defaultdict(float)
	freq_dict=collections.defaultdict(float)
	for entry in gramdict:
		#remember that string is our variable
		if string in entry:
			#print len(item), item, gramdict[item], item.index(string)
			#exclude if last in gram
			if len(entry) == entry.index(string)+1:
 				pass
			else:
				##count counts instances of word under consideration
				temp_dict['count']=temp_dict['count'] + 1
				#this counts instances of word under consideration followed by word in entry
				temp_dict[entry[entry.index(string)+1]]=temp_dict[entry[entry.index(string)+1]]+1
	for entry in temp_dict:
		if not entry == 'count' and not entry =='Part':
			#print entry, temp_dict[entry], temp_dict['count']
			freq_dict[entry]=temp_dict[entry]/temp_dict['count']#*(worddict[entry]/5)
	#stolen from: http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
	freq_dict_sorted=sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
	return freq_dict_sorted


def sentbuilder(gramdict, worddict, startstring, endstring):
	#start with ".", pick follow up from list of top fifty, until you hit "." again
	sentence=[]
	#total word count
	total=sum(worddict.values())
	word=random.choice(generatemachine(gramdict, worddict, ".")[0:10])[0]
	sentence.append(word)
	while word not in endstring:
		wordlist= generatemachine(gramdict, worddict, word)
		if "." in [i[0] for i in wordlist][0]: 
			print  "breaking"
			probs=[float(worddict[s])/total for s in sentence]
			probs=math.log(np.prod(np.array(probs)))
			#print "probability of sentence", probs
			return (sentence, probs)
		else:
			word = random.choice(wordlist[0:10])[0]
			sentence.append(word)
	#calculate probability of sentence
	probs=[float(worddict[s])/total for s in sentence]
	probs=math.log(np.prod(np.array(probs)))
	#print "probability of sentence", probs
	return (sentence, probs)


def main(iter):
	dir="out"
	files=[i for i in os.listdir(dir) if not i.startswith(".")]
	worddicti=dictmaker(files, 1)
	worddicti={k[0]:worddicti[k] for k in worddicti}
	print worddicti['The']
	#standard count for "." is 34607
	print "the word dictionary is {} items long".format(len(worddicti))
# 	for entry in worddicti:
# 		if worddicti[entry] > 20:
# 			print entry[0]
	gramdicti=dictmaker(files, 4)
	print "the gram dictionary is {} items long".format(len(gramdicti))
	for i in range(iter):
		output_sentence, output_prob=sentbuilder(gramdicti,worddicti, ".", ".!?\"")
		if output_prob > - 100:
				print "Aristotle says: \"{}\"".format(" ".join(output_sentence))
				#print "Aristotle says: \"{}\" \n with a probability of {}".format(" ".join(output_sentence), output_prob)
	#frequencies=generatemachine(string, gramdicti)
	
	


main(100)

#generate outputsentences






# main:
# dictionary
# probs
# output

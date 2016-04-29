import re, numpy as np, codecs, os, nltk, collections, random, math
from string  import digits, punctuation
import generatortools as gt




 	
def sentbuilder(startstring, endstring, worddict, *args):
	"takes word lists"
	#start with ".", pick follow up from list of top fifty, until you hit "." again
	sentence=[startstring]
	#total word count
	total=sum(worddict.values())
	first_word=gt.generatemachine(worddict, args[0], startstring)#random.choice(generatemachine(worddict, arg[0], "."))
	first_word_sorted=sorted(first_word.items(), key=lambda x: x[1], reverse=True)
	word=random.choice(first_word_sorted)[0]
	#print word
	sentence.append(word)
 	while word not in endstring:
 		prev_word=sentence[len(sentence)-2]
 		#print prev_word
 		current_word=sentence[len(sentence)-1]
 		#print current_word
 		word_less_two=gt.generatemachine(worddict, args[1],  prev_word)
 		#print "word less 2 length ", len(word_less_two)
 		word_less_one=gt.generatemachine(worddict, args[0], current_word)
 		#print "word less 1 length ", len(word_less_one)
 		freqs={k:v*word_less_two.get(k, 1) for k, v in word_less_one.items()}
 		#print "word less 2 UPDATED length ", len(word_less_two)
 		next_word_sorted=sorted(freqs.items(), key=lambda x: x[1], reverse=True)
 		#word=next_word_sorted[0][0]
 		word=random.choice(next_word_sorted[:5])[0]
 		sentence.append(word)
 	else:
 		out=" ".join(sentence).lstrip(".")
 		print "Aristotle says: "
 		print out, "\n"
 		
 		
# 		
# 		print word_less_two
# 		print word_less_one
# 		break
		# word_less_one=gt.generatemachine(worddict, args[0], word)[0][0]
# 		print "word 1", word_less_one
# 		word_less_two=gt.generatemachine(worddict, args[1],  word)[0][0]
# 		print "word 2", word_less_two
# 		word = word_less_one#random.choice(word_less_one[0:20])[0]
		#print "word", word
# 		sentence.append(word)
# 	#calculate probability of sentence
# 	probs=[float(worddict[s])/total for s in sentence]
# 	probs=math.log(np.prod(np.array(probs)))
# 	#print "probability of sentence", probs
	#return (sentence, probs)	
	#
##need to use word dict counts instead of overall-count for trigrams, right???
## <s> and </s>
## use bigram probs for evaluation



dir="out"
files=[os.path.join("out", i) for i in os.listdir(dir) if not i.startswith(".")]
#print "We're working with these files: ", files
print "Making the word dicti"
worddicti=gt.dictmaker(files, 1)
print "Making the bigram dicti"
bigramdicti=gt.dictmaker(files, 2)
print "Making the trigram dicti"
trigramdicti=gt.dictmaker(files, 3)
print "Starting the sentence builder"
# x=gt.generatemachine(worddicti, bigramdicti, "the")
# y=gt.generatemachine(worddicti, trigramdicti, "the")
for item in range(0,100):
	sentbuilder(".",".;()", worddicti, bigramdicti, trigramdicti)


# for item in worddicti:
# 	print type(item[0])

# following word: 
# sorted by probability -1
# then probability -2 --> multiply

# 	#stolen from: http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

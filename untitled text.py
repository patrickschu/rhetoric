import re, datetime, time
from string import punctuation

x=time.strftime("%m/%d/%Y")
print x
# cleantext=["...", "I.", "assi", "...assi", "go", "home", "well-desvered", ".", "!"]
# print cleantext
# endtext=[i.strip(punctuation) for i in cleantext if re.search("\w+", i)]
# print endtext

# tt={("i", "do.", "."): 3, (".the", "do.g"): 23, ("your", "facie"): 33}
# #print tt
# 
# 
# for item in tt:
# 	if "." in item:
# 		print item
t=b"I love you"

print type(t)
	
# t=[("I", 0.1),("be", 1),("a", 2),("son", 0.04)]
# r=[("I", 100),("a", 100), ("son",100),("tree", 10)]
# 
# t=dict(t)
# r=dict(r)
# print r
# print t
# #print d
# d2={k:v+r.get(k, 0) for k, v in t.items()}
# t=r.update(d2)()
# print t


#key
#secret


 


#s=[i for i in t if i[0] in r]

#merge on tuple[0]; while merging, multiply tuple[1]. keep all items



# s=zip(t,r)
# print s
# 
# print list(t)[0]+10


# 	". The world is good. 
# 	
# 	"for "." produce most likely to follow == X., world.
# 	"for "." produce most likely to follow +2== Y., assi
# 	" output "world". 
# 	"for "world" produce most likely to follow == Xworld, is.
# 	"for "world" produce most likely to follow +2== Y.
# 	"output calculation Y. and Xworld, gives us "is"

	
		# if "." in [i[0] for i in wordlist][0]: 
# 			print  "breaking"
# 			probs=[float(worddict[s])/total for s in sentence]
# 			probs=math.log(np.prod(np.array(probs)))
# 			#print "probability of sentence", probs
# 			return (sentence, probs)
# 		else:

from twython import Twython

login=open("twitter_keys.txt", "r")
login=login.read()
key=login.split(",")[0]
secret=login.split(",")[1]
token=login.split(",")[2]
token_secret=login.split(",")[3]
arisbotle= Twython(key, secret,token,token_secret)
arisbotle.update_status(status='How hard can this be?')

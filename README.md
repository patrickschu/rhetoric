## DWRL project "Digital Archives"

### Getting to know Arisbotle


### Running the Arisbotle script

Open the "Terminal" app and navigate to the folder the script is saved in, e.g. 
`cd Downloads/rhetoric-master`

then type 

`python arisbotle.py "folder_of_textfiles"`

where the folder_of_textfiles is a directory that contains the text files you want to train the machine on and it will run. 
Additional settings, to be added in this order after the folder_of_textfiles:

`iter = 100, probability_cutoff = - 40 , threshold = 10, tweet=False`

Where `iter` is the number of iterations, i.e. the number of sentences to generate. The `probability_cutoff` specifies the mininum probability (in log space) of the sentence to be published / tweeted. `threshold` determines the number of words the sentencebuilder considers when picking the word to follow. Larger numbers give more variety, smaller numbers higher quality sentences. `tweet` turns the Twittter functionality on (True) and off (False). The values shown above are the defaults the script will use unless told otherwise. 

## How to cite 





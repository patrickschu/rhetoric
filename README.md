### Digital Writing and Research Lab: "Digital Archiving and the object"

#### Who is Arisbotle?

Arisbotle is a speech bot that creates and tweets sentences [here](https://twitter.com/Arisb0tle). He learns from a corpus of classical writings and uses a trigram language model to create new sentences of his own. He is part of a research project at the [Digital Writing and Research Lab](http://www.dwrl.utexas.edu/) at [UT Austin](https://twitter.com/TexasSports). You can read more about this project [here](http://www.dwrl.utexas.edu/2016/04/19/reviving-the-archive-aristotle-re-animated/). 


#### Running the Arisbotle script

Download the code from https://github.com/patrickschu/rhetoric.

Open the "Terminal" app and navigate to the folder the script is saved in, e.g. 

`cd Downloads/rhetoric-master`

then type 

`python arisbotle.py "folder_of_textfiles"`

where the folder_of_textfiles is a directory that contains the text files you want to train the machine on. It's easiest if you keep in the same folder the script is in. Additional settings, to be added in this order after the folder_of_textfiles:

`iter = 100, probability_cutoff = - 40 , threshold = 10, tweet=False`

Where `iter` is the number of iterations, i.e. the number of sentences to generate. The `probability_cutoff` specifies the mininum probability (in log space) a sentence needs to meet to be published / tweeted. `threshold` determines the number of words the sentence building algorithm considers when picking a word Y to follow word X. Larger numbers give more variety, smaller numbers higher quality sentences. `tweet` turns the Twittter functionality on (`True`) and off (`False`). The values shown above are the defaults the script will use unless told otherwise. Note that for Twitter to work you need to have a file with the tokens and secrets to log into the Twitter API. 


<!--- 
#### How to cite this piece of code
Schultz, Patrick. Arisbotle: A philosophical . Computer software. May 2016. https://github.com/patrickschu/rhetoric/blob/master/arisbotle.py.
---> 





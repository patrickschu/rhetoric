### Digital Writing and Research Lab: "Digital Archiving and the Object"

This repository contains some code created for the "Digital Archiving and the Object" project at the DWRL @ UT Austin in the Spring of 2016, among them our beloved speech bot Arisbotle. 

#### Who is Arisbotle?

Arisbotle is a speech bot that creates and [tweets](https://twitter.com/Arisb0tle) sentences. He learns from a corpus of classical writings and uses a trigram language model to create new sentences of his own. He is part of a research project at the [Digital Writing and Research Lab](http://www.dwrl.utexas.edu/) at [UT Austin](https://twitter.com/TexasSports). You can read more about this project [here](http://www.dwrl.utexas.edu/2016/04/19/reviving-the-archive-aristotle-re-animated/). 


#### Running the Arisbotle script

Download the code from https://github.com/patrickschu/rhetoric.

Open the "Terminal" app and navigate to the folder the script is saved in, e.g. 

`cd Downloads/rhetoric-master`

then type 

`python arisbotle.py "folder_of_textfiles"`

where the folder_of_textfiles is a directory that contains the text files you want to train the machine on. It's easiest if you keep in the same folder the script is in. Additional settings, to be added in this order after the folder_of_textfiles:

`iter = 100, probability_cutoff = - 40 , threshold = 10, tweet=False`

Where `iter` is the number of iterations, i.e. the number of sentences to generate. The `probability_cutoff` specifies the mininum probability (in log space) a sentence needs to meet to be published / tweeted. `threshold` determines the number of words the sentence building algorithm considers when picking a word Y to follow word X. Larger numbers give more variety, smaller numbers higher quality sentences. `tweet` turns the Twittter functionality on (`True`) and off (`False`). The values shown above are the defaults the script will use unless told otherwise. Note that for Twitter to work you need to have a file with the tokens and secrets to log into the Twitter API. 

### Etc.

Citation. 
Schultz, Patrick. Arisbotle: A philosophical speech bot, 2016, https://github.com/patrickschu/rhetoric/ [Online; accessed XXXX-XX-XX].

The MIT License (MIT)
Copyright (c) 2016 Patrick Schultz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<!--- 
#### How to cite this piece of code
Schultz, Patrick. Arisbotle: A philosophical . Computer software. May 2016. https://github.com/patrickschu/rhetoric/blob/master/arisbotle.py.
---> 





# html-highlight-
This is a python script that highlights similar sentences in a series of input text files using `html` and outputs them in another `html` file. This script finds similar sentences using the `TfidfVectorizer` library, which works by means of *Term Frequency* (number of repetitions of a word in a sentence / number of words in the sentence) and *Inverse Document Frequency* (log (number of sentences / number of sentences containing the word)) matrix of each sentence, 
and colors the highlights using the `matplotlib.cm.colormap.`

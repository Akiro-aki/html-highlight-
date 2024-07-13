import os
# import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np
import re



def readFile (textFiles ):
    texts=[]
    sent_s=[]
    html_sent_s=[]
    for textfile in textFiles:
        with open(textfile , "r") as textfile:
            texts.append(textfile.read())
    for text in texts:
         pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
         sentence = re.split(pattern, text)
         for snt in sentence:
          sent_s.append( snt )
    return sent_s

def similar(sent_s):
    vectorizer = TfidfVectorizer().fit_transform(sent_s)
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)
    print(cosine_matrix)
    return cosine_matrix


def Getcolors(similarity_matrix):
    norm = mcolors.Normalize(vmin=0, vmax=1)
    colormap = cm.get_cmap()
    colors = colormap(norm(similarity_matrix))

    avg_similarity = np.mean(similarity_matrix, axis=1)
    colors = colormap(norm(avg_similarity))
    return colors

def html(sentences, colors):
    html_sentences = []
    for i, sentence in enumerate(sentences):
        color = mcolors.to_hex(colors[i][:3])
        html_sentences.append(f'<span style="background-color: {color}">{sentence}</span>')
    return '<br>'.join(html_sentences)


def html_hilghlight (textFiles) :
    sente =readFile(textFiles)
    SimMat = similar (sente)
    color = Getcolors(SimMat)
    html_text = html (sente,color)
    return html_text
   

textFiles = ['path to the text file ']
output=html_hilghlight (textFiles)
print(cosine_similarity)
with open ('html highlighted.html', 'w') as outputFile:
    outputFile.write(output)
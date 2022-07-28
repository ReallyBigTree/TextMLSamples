#TextBlob

#pip install spacytextblob
# # python -m textblob.download_corpora
# python -m spacy download en_core_web_sm


#https://www.numpyninja.com/post/text-summarization-through-use-of-spacy-library

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import tkinter as tk
from tkinter import filedialog

stopwords = list(STOP_WORDS)
punctuation = punctuation + '\n'









def UploadAction(event=None):
    filename = filedialog.askopenfilename()
   # print('Selected:', filename)

    with open(filename, "r") as f:
        lines = f.read()

    print(lines)
    print()


    ##Tokenize words
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(lines)
    tokens = [token.text for token in doc]
    print(tokens)

    ##Get word frequencies
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    print(word_frequencies)

    ##Normalize frequencies (max frequency / all frequency)
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    print(word_frequencies)

    ##Tokenize sentences
    sentence_tokens= [sent for sent in doc.sents]
    print(sentence_tokens)

    ##get sentence scores (adding and comparing word frequencies of each sentence)
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                 sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                 sentence_scores[sent]+=word_frequencies[word.text.lower()]
    print(sentence_scores)


    select_length=int(len(sentence_tokens)*0.3)
    select_length
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    print(summary)

    final_summary=[word.text for word in summary]
    final_summary
    summary=''.join(final_summary)
    summary
    print(summary)



root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()
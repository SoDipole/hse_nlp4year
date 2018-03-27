# coding: utf-8

import numpy as np
import pandas as pd
import regex as re
import os
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
from preprocessing import tokenize
import time



def sentence_split(text):
    # не state-of-art, но для данного случая подойдет
    abbr = re.compile('(?:\s|^)((?:[а-яё]{1,3}\.)*[а-яё]{1,3}\.)', flags=re.I)
    for substr in re.findall(abbr, text):
        text = text.replace(substr, substr.replace('.', '<dot>'))
    sentences = re.split('[!?;\.]+', text)
    for i in range(len(sentences)):
        sentences[i] = sentences[i].replace('<dot>', '.')
    return [ i for i in sentences if i]

neg = pd.read_csv('negative.csv', sep = ';', header=None)
pos =  pd.read_csv('positive.csv', sep = ';', header=None)
sentences = []
for corp in [neg, pos]:
	for row in corp[3]:
	    sentences.extend([tokenize(sentence) for sentence in sentence_split(row)])

print(str(len(sentences))+' sentences')

start = time.time()
model = Word2Vec(sentences, size=200, window=5, min_count=3, sg=0)
print("--- %s seconds ---" % (time.time() - start))

# сохранить модель (ее можно потом дообучить)
model.save('tweets.w2v')

vectors = model.wv

# сохранить только векторы (дообучить нельзя, но работает быстрее)
vectors.save_word2vec_format('tweets.bin', binary=True)


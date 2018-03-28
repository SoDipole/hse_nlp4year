import pymorphy2
import math
import re
import pandas as pd
#print (m.parse('кошки')[0].normal_form)



#
# dataframe = pd.read_csv('negative.csv', header=None, sep=';')
# neg_raw = dataframe[3]
# neg_raw = ' '.join(neg_raw)

# dataframe = pd.read_csv('positive.csv', header=None, sep=';')
# pos_raw = dataframe[3]
# pos_raw = ' '.join(pos_raw)



def preprocess(corpus, sublist = ['.',',','?',':',';','-','!',':)',':(',')','(','0','1','2','3','4','5','6','7','8','9','[',']']):
    for i in sublist:
       corpus =  corpus.replace(i, ' ')
    corpus = re.sub(' +', ' ', corpus)
    corpus = corpus.split(' ')
    return corpus


def lemmatize(corpus):
    m = pymorphy2.MorphAnalyzer()
    for i in range (0, len(corpus)):
        corpus[i] = m.parse(corpus[i])[0].normal_form
    return corpus
#
# file = open('neg_lemmatized.txt', 'w', encoding='utf-8')
# file.write(' '.join(lemmatize(preprocess(neg_raw))))
# file.close()

def frequency(word, corpus):
    w = 0
    n = 0
    for i in corpus.split():
        n = n+1
        if i == word:
            w = w+1
    if w != 0:
        return 1/math.log10(1/(w/n))
    else:
        return 0





def word_polarity(word, pos, neg):
    pind = frequency(word, pos)
    nind = frequency(word, neg)
   # if frequency(word, pos) > frequency(word, neg):
   #     return pos
    #else:
     #   return neg
    res =  pind-nind
    if res >= 0.008:
        des = 'positive'
    elif res <= -0.005:
        des = 'negative'
    else:
        des = 'uncertain or ambiguous'
    return [pind, nind, pind-nind, des]


polarity = {}
file = open('pos_lemmatized.txt', 'r', encoding='utf-8')
pos = file.read()
file.close()
file = open ('neg_lemmatized.txt', 'r', encoding='utf-8')
neg = file.read()
file.close()

file = open('w2v_all_clean.txt', 'r', encoding='utf-8')
target_words = file.read().split('\n')
file.close()
for w in target_words:
    print (w)
    if w != '':
        polarity[w] = word_polarity(w, pos, neg)
file = open ('results_polarity.txt', 'w', encoding='utf-8')
out = 'lexeme' + ':' + 'positive index' +' : ' + 'negative index' + ' : ' + 'total idex' + ' : ' + 'decision'
out = '\n'.join([l + ' : ' + ' : '.join([str(c) for c in polarity[l]]) for l in polarity])
file.write(out)
file.close()
print (word_polarity('',pos, neg))
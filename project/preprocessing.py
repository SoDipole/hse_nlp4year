# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from __future__ import division
import numpy as np
import pandas as pd
import json
from pymystem3 import Mystem
import re
import io
import itertools

analyzer = Mystem()
strip_characters = '!`«»‰~@\'▲▼„"#$%^&*()_-+=[]\{\}°:;|•.,<>?/————–'
split_reg = re.compile('[\s\(\)\.,;"«»\'\[\]&<>]+')
punctuation = set(strip_characters)
num_reg = re.compile(r'[0-9)(:\-/№#]+?')
pos_map = {'A': 'ADJ',
            'ADV': 'ADV',
            'ADVPRO': 'PRON',
            'ANUM': 'ADJ',
            'APRO': 'PRON',
            'COM': 'NOUN',
            'CONJ': 'CCONJ',
            'INTJ': 'PART',
            'NUM': 'NUM',
            'PART': 'PART',
            'PR': 'ADP',
            'S': 'NOUN',
            'SPRO':'PRON',
            'V': 'VERB'}

with open('stop_words.json') as file:
        stop_words = json.load(file)

adress_reg = re.compile('(?:г\.|город|ул\.|улица|дом|д\.|стр\.|строение|проезд|бульвар)\s*[А-ЯЁа-яёa-z0-9\-\.]+?[,\s$][0-9]*')
adress_keywords_reg = re.compile('(?:г\.|город|ул\.|улица|дом|д\.|стр\.|строение|проезд|бульвар)')
nickname_reg = re.compile('@[a-zA-Z_\-0-9]+?[\s\.,]')

def remove_nickname_(string):
    string = nickname_reg.sub(string=string, repl=' ')
    return string

def tokenize(string, need_pos=False, remove_nickname=True):
    if remove_nickname:
        tokens = [lemmatize_pos_tag(i.lower().strip(strip_characters), need_pos=need_pos) 
                  for i in re.split(split_reg, remove_nickname_(string)) if i.strip(strip_characters) and i not in punctuation 
                  and i not in stop_words and not num_reg.match(i)]
    else:
        tokens = [lemmatize_pos_tag(i.lower().strip(strip_characters), need_pos=need_pos) 
                  for i in re.split(split_reg, string) if i.strip(strip_characters) and i not in punctuation 
                  and i not in stop_words and not num_reg.match(i)]
    valid_tokens = [token for token in tokens if token]
    return valid_tokens

def lemmatize_pos_tag(token, need_pos):
    if need_pos:
        analysis = analyzer.analyze(token)
        try:
            lemma = analysis[0]['analysis'][0]['lex']
            pre_pos = re.split('[,=]+?', analysis[0]['analysis'][0]['gr'])[0]
            pos = pos_map[pre_pos]
            lemma = lemma+'_'+pos
        except (KeyError, IndexError) as e:
            lemma = token
            pos = 'NOUN'
            lemma = lemma+'_'+pos
    else:
        try:
            lemma = analyzer.lemmatize(token)[0]
        except (KeyError, IndexError) as e:
            lemma = token
    return lemma


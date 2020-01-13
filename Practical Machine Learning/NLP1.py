#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:50:02 2019

@author: student
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
print(ps.stem('working'))


#Does not Understand Context and just removes es from the end.
ps=PorterStemmer()
print(ps.stem('increases'))

#Considers Context of the word and thus gives better Output
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
ps=WordNetLemmatizer()
print(ps.lemmatize('increases'))

#Stemming is faster but is less accurate
#Lemmatizer is slower but much more accurate as it considers the context as well

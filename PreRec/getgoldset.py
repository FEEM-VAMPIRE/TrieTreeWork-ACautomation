# -*- coding: utf-8 -*-  
import ahocorasick as AC
import pickle
import re
import time

goldset = []
with open('sys-link-sm-0.tab', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.split('\t')[2]
        if word not in goldset:
            goldset.append(word)

#goldset
#goldlen = len(goldset)
with open('goldsetofchen', 'w', encoding='utf-8') as file:
    for word in goldset:
        file.write(word+'\n')


goldset = []
with open('2017-ENG-eval', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.split('\t')[2]
        if word not in goldset:
            goldset.append(word)

#goldset
#goldlen = len(goldset)
with open('ungetsetofzheng', 'w', encoding='utf-8') as file:
    for word in goldset:
        file.write(word+'\n')

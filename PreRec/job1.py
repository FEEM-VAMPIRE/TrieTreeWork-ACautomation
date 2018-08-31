# -*- coding: utf-8 -*-  
import ahocorasick as AC
import pickle
import re
import time

goldset = []
with open('goldofjob1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.split('\n')[0]
        if word not in goldset:
            goldset.append(word)

#goldset
goldlen = len(goldset)

guessset = []
with open('formatLinkjob1chen.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.split('\t')[1]
        if word not in guessset:
            guessset.append(word)

#guessset
guesslen = len(guessset)
true_predict_Word=0
for word in goldset:
    if word in guessset or word.title() in guessset or word.lower() in guessset or word.upper() in guessset:
        true_predict_Word += 1
    #else : 
    #    with open('wrongresultofz8.23.15', 'a', encoding='utf-8') as file:
    #        file.write(word+'\n')

#true_predict_Word
precision = true_predict_Word/guesslen
recall = true_predict_Word/goldlen
print("guessset: ",guesslen,"\tgoldset: ",goldlen,"\tTruePositive: ",true_predict_Word)
print("\nprecision: ",precision,"\trecall:",recall)

"""
#ingoldnotinguess
for word in goldset:
    firfam = re.split(' |\'|\.|-', word)
    #firfam = word.split()
    temp = firfam[0]
    for i in range(1,len(firfam)):
        if(firfam[i]!=""):
            temp += " " + firfam[i]
    if temp not in guessset:
        with open('ingoldnotinguess', 'a', encoding='utf-8') as file:
            file.write(word+'\n')

#inguessnotingold
words_num = 0
for wordguess in guessset:
    isin = False
    for word in goldset:
        firfam = re.split(' |\'|\.|-', word)
        #firfam = word.split()
        temp = firfam[0]
        for i in range(1,len(firfam)):
            if(firfam[i]!=""):
                temp += " " + firfam[i]
        if(temp == wordguess):
            isin = True
            break
    if isin == False :
        words_num+=1
        with open('inguessnotingold', 'a', encoding='utf-8') as file:
            file.write(wordguess+'\n')

print(words_num)

"""
'''
lowerWordNum = 0
for word in goldset:
    if word.lower()==word:
        lowerWordNum += 1

print(lowerWordNum)
'''
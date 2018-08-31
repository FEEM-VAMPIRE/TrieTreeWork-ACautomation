# -*- coding: utf-8 -*-  
import ahocorasick as AC
import pickle
import re
import time

start_time = time.time()
def getNum(firName):
    filename = firName[0:firName.index(':')]
    num_end = len(firName)
    num_start = firName.index(':') + 1
    mid = firName.index('-')
    left = int(firName[num_start:mid])
    right = int(firName[mid+1:num_end])
    return filename,left,right

isSingleset = []
wordset = []
linkset = []
filenameset = []
with open('formatLink2.2-c1.txt', 'r', encoding='utf-8', errors="ignore") as file:
    for line in file:
        word,link = line.split('\t')[1:3]
        wordset.append(word)
        if len(word.split()) == 1:
            isSingleset.append(True)
        else :
            isSingleset.append(False)
        filename,start_num,end_num = getNum(link)
        linkset.append([start_num,end_num])
        filenameset.append(filename)

totalLen = len(wordset)

for i in range(totalLen):
    isCross = False
    substr = wordset[i]
    filename = filenameset[i]
    sub_start_num, sub_end_num = linkset[i]
    if isSingleset[i]:
        for j in range(totalLen):
            if not isSingleset[j] and substr in wordset[j] and filename == filenameset[j]:
                whlstr = wordset[j]
                whl_start_num, whl_end_num = linkset[j]
                if whl_start_num <= sub_start_num and sub_end_num <= whl_end_num:
                    isCross = True
                    break
    if isCross:
        continue            
    else :
        with open("formatLink2.2-noCross-c1.txt", 'a',encoding='utf-8') as file:
            file.write("ZJU\t" + substr +"\t" + filename +':'+str(sub_start_num)+'-'+str(sub_end_num)+ "\n")


print(time.time()-start_time)
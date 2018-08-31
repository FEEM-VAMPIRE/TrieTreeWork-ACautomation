# -*- coding: utf-8 -*-  
import ahocorasick as AC
import pickle
import re
import time
#1.4 update to clear something unuseful 
#set up a ahocroasick tree
#B is the doc tree, C is the n.but not noun tree,  D is the not noun tree
start_time = time.time()
B = AC.Automaton()
C = AC.Automaton()
D = AC.Automaton()

with open('namelist.txt', 'r') as _namelist:
    A = _namelist.read()

namelist = A.split('\n')

_wor = []
_idx = []
for filename in namelist:
    if 'ENG_DF' in filename:
        wholefilename = 'df/'+ filename +'.xml'
    else:
        wholefilename = 'nw/'+ filename +'.xml'
    print(wholefilename)
    #there is UnicodeDecodeError: 'gbk' codec can't decode byte 0x9d in position 704: illegal multibyte sequence 
    #error in file df/ENG_DF_001471_20160105_G00A0G3W2.xml
    with open(wholefilename, 'r', errors='ignore') as file:
        A = file.read()
    #
    #B = pickle.dumps(A)
    #A = "xiaoming xiaoming qu shang xue qu le xiaoming mama song de ta"
    #for _,word in enumerate(re.split('\n|!|\?|\.|\"|<|>|=|:',A)):
    i = 0
    a = A
    lenA = len(a)
    for _,word in enumerate(re.split('\/|-|,| |\n|!|\?|\.|\"|<|>|=|\'|:',A)):
        aindex = a.index(word)
        wordlen = len(word)
        wordStart = aindex + i
        i = wordStart + wordlen
        wordEnd = i-1
        a = a[aindex+wordlen : lenA-1]
        if word in _wor:
            _idx[_wor.index(word)].append(filename+':'+str(wordStart)+'-'+str(wordEnd))
        else:
            _wor.append(word)
            _idx.append([filename+':'+str(wordStart)+'-'+str(wordEnd)])
    

# 向trie树中添加单词
for index,word in enumerate(_wor):
    B.add_word(word, (_idx[_wor.index(word)], word))

with open('vnnvadvadj.txt', 'r') as file:
    unnounlyset = file.read()


with open('notNoun.txt', 'r') as file:
    unnounset = file.read()


unnounlyset = unnounlyset.split('\n')
for index,word in enumerate(unnounlyset):
    C.add_word(word, (index, word))


unnounset = unnounset.split('\n')
for index,word in enumerate(unnounset):
    D.add_word(word, (index, word))
# 用法分析add_word(word,[value]) => bool
# 根据Automaton构造函数的参数store设置，value这样考虑：
# 1. 如果store设置为STORE_LENGTH，不能传递value，默认保存len(word)
# 2. 如果store设置为STORE_INTS，value可选，但必须是int类型，默认是len(automaton)
# 3. 如果store设置为STORE_ANY，value必须写，可以是任意类型

print("over")

# 将trie树转化为Aho-Corasick自动机
B.make_automaton()
C.make_automaton()
D.make_automaton()
#test
#B.get('NJ')
#B.get('jacobj')
print(time.time()-start_time)

aliasset = []
with open('PreRec/goldset/goldsetofchen', 'r', encoding='utf-8') as file:
    for line in file:
        aliasset.append(line.rstrip('\n'))

#aliasset

def getNum(firName):
    num_end = len(firName)
    num_start = firName.index(':') + 1
    mid = firName.index('-')
    left = int(firName[num_start:mid])
    right = int(firName[mid+1:num_end])
    return left,right
#
print(time.time()-start_time)
start_time3 = time.time()
percent = 0
word_nums = 0
for idx,alias in enumerate(aliasset):
    if(idx%1000000 == 999999):
        percent = percent + 5
        print("progressing: ---", percent,"%---")
        print("timeUsing:  ",time.time()-start_time3)
    firfam = alias.split()
    if len(firfam) == 2:
        if (D.exists(firfam[0].lower()) and D.exists(firfam[1].lower())):
            continue
        elif(B.exists(firfam[0]) and B.exists(firfam[1])):
            firName = B.get(firfam[0])
            famName = B.get(firfam[1])
            for i in range(len(firName[0])):
                for j in range(len(famName[0])):
                    filename = firName[0][i][0:firName[0][i].index(':')]
                    if filename in famName[0][j]:
                        fir_start_num, fir_end_num = getNum(firName[0][i])
                        fam_start_num, fam_end_num = getNum(famName[0][j])
                        if fam_start_num - fir_end_num == 2:
                            with open("resultofgoldwordofchen", 'a',encoding='utf-8') as file:
                                file.write("ZJU\t" + alias +"\t" + filename +':'+str(fir_start_num)+'-'+str(fam_end_num)+ "\n")
                                word_nums = word_nums+1

    #
    elif len(firfam) == 1:  
        if(B.exists(alias) and not C.exists(alias.lower()) and not D.exists(alias.lower()) and not alias.isdigit()):
        	if(alias[-1] == 's' and C.exists(alias[0:-1].lower())):
        		continue
        	else:
	            item = B.get(alias)
	            with open("resultofgoldwordofchen", 'a') as file:
	                #file.write(item[1])
	                for locations in item[0]:
	                    file.write("ZJU\t" + item[1] +"\t" + locations+ "\n")
	                    word_nums = word_nums+1
#

print("word_nums: ", word_nums)
print(time.time()-start_time)

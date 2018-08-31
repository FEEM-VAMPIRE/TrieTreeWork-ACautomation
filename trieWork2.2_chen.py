# -*- coding: utf-8 -*-  
import ahocorasick as AC
import pickle
import re
import time
#2.2 still update to clear something unuseful 
#set up a ahocroasick tree
#B is the doc tree, C is the n.but not noun tree,  D is the not noun tree (with month and digit)
#E is the prep pron tree
start_time = time.time()
B = AC.Automaton()
C = AC.Automaton()
D = AC.Automaton()
E = AC.Automaton()
with open('namelist.txt', 'r') as _namelist:
    A = _namelist.read()

namelist = A.split('\n')

_wor1 = []
_idx1 = []
_wor2 = []
_idx2 = []
_wor3 = []
_idx3 = []

for filename in namelist:
    if 'ENG_DF' in filename:
        wholefilename = 'df/'+ filename +'.xml'
    else:
        wholefilename = 'nw/'+ filename +'.xml'
    print("processing:  ",wholefilename," --*.*.*.*--")
    with open(wholefilename, 'r', encoding='utf-8') as file:
        A = file.read()
    #B = pickle.dumps(A)
    #A = "xiaoming xiaoming qu shang xue qu le xiaoming mama song de ta"
    #for _,word in enumerate(re.split('\n|!|\?|\.|\"|<|>|=|:',A)):
    i = 0
    a = A
    lenA = len(a)
    memo_wordforDouble = ""
    memo_wordforTrible = ""
    memo_wordStartforDouble=0
    memo_wordStartforTrible=0
    for index,word in enumerate(re.split('\/|-|,| |\n|!|\?|\.|\"|<|>|=|\'|:',A)):
        if(word == ""):
            continue
        else:
            aindex = a.index(word)
            wordlen = len(word)
            wordStart = aindex + i
            i = wordStart + wordlen
            wordEnd = i-1
            a = a[aindex+wordlen : lenA]
            if word in _wor1:
                _idx1[_wor1.index(word)].append(filename+':'+str(wordStart)+'-'+str(wordEnd))
            else:
                _wor1.append(word)
                _idx1.append([filename+':'+str(wordStart)+'-'+str(wordEnd)])
            if index>1 :
                doubleWord = memo_wordforDouble + " " + word
                if doubleWord in _wor2:
                    _idx2[_wor2.index(doubleWord)].append(filename+':'+str(memo_wordStartforDouble)+'-'+str(wordEnd))
                else:
                    _wor2.append(doubleWord)
                    _idx2.append([filename+':'+str(memo_wordStartforDouble)+'-'+str(wordEnd)])
            if index>2 :
                tribleWord = memo_wordforTrible + " " + memo_wordforDouble + " " + word
                if tribleWord in _wor3:
                    _idx3[_wor3.index(tribleWord)].append(filename+':'+str(memo_wordStartforTrible)+'-'+str(wordEnd))
                else:
                    _wor3.append(tribleWord)
                    _idx3.append([filename+':'+str(memo_wordStartforTrible)+'-'+str(wordEnd)])
            memo_wordStartforTrible = memo_wordStartforDouble
            memo_wordStartforDouble = wordStart
            memo_wordforTrible = memo_wordforDouble
            memo_wordforDouble = word
    

# 向trie树中添加单词
for index,word in enumerate(_wor1):
    B.add_word(word, (_idx1[_wor1.index(word)], word))

for index,word in enumerate(_wor2):
    B.add_word(word, (_idx2[_wor2.index(word)], word))

for index,word in enumerate(_wor3):
    B.add_word(word, (_idx3[_wor3.index(word)], word))

with open('vnnvadvadj.txt', 'r') as file:
    unnounlyset = file.read()

with open('v..txt', 'r') as file:
    unnounset = file.read()

with open('preppron.txt', 'r') as file:
    preproset = file.read()

unnounlyset = unnounlyset.split('\n')
for index,word in enumerate(unnounlyset):
    C.add_word(word, (index, word))

unnounset = unnounset.split('\n')
for index,word in enumerate(unnounset):
    D.add_word(word, (index, word))

preproset = preproset.split('\n')
for index,word in enumerate(preproset):
    E.add_word(word, (index, word))

# 用法分析add_word(word,[value]) => bool
# 根据Automaton构造函数的参数store设置，value这样考虑：
# 1. 如果store设置为STORE_LENGTH，不能传递value，默认保存len(word)
# 2. 如果store设置为STORE_INTS，value可选，但必须是int类型，默认是len(automaton)
# 3. 如果store设置为STORE_ANY，value必须写，可以是任意类型

# 将trie树转化为Aho-Corasick自动机
B.make_automaton()
C.make_automaton()
D.make_automaton()
E.make_automaton()
#test
#B.get('NJ')
#B.get('jacobj')
print(time.time()-start_time)

with open('aliassetNEW.pkl', 'rb') as file:
    aliasset = pickle.load(file)

def getNum(firName):
    num_end = len(firName)
    num_start = firName.index(':') + 1
    mid = firName.index('-')
    left = int(firName[num_start:mid])
    right = int(firName[mid+1:num_end])
    return left,right

print(time.time()-start_time)


start_time3 = time.time()
percent = 0
word_nums = 0
for idx,alias in enumerate(aliasset):
    if(idx%1000000 == 999999):
        percent = percent + 5
        print("progressing: ---", percent,"%---")
        print("timeUsing:  ",time.time()-start_time3)
    #firfam = alias.split()
    firfam = re.split(' |\'|\.|-', alias)
    if alias == alias.lower() or E.exists(firfam[0].lower()):
        continue
    elif len(firfam) > 3:
        temp = []
        strtemp = firfam[0]
        for i in range(1,3):
            if(firfam[i]!=""):
                strtemp += " " + firfam[i] 
        temp.append(strtemp)
        strtemp = firfam[3]
        for i in range(4,len(firfam)):
            if(firfam[i]!=""):
                strtemp += " " + firfam[i]
        temp.append(strtemp)
        if(B.exists(temp[0]) and B.exists(temp[1])):
            firName = B.get(temp[0])
            famName = B.get(temp[1])
            for i in range(len(firName[0])):
                for j in range(len(famName[0])):
                    filename = firName[0][i][0:firName[0][i].index(':')]
                    if filename in famName[0][j]:
                        fir_start_num, fir_end_num = getNum(firName[0][i])
                        fam_start_num, fam_end_num = getNum(famName[0][j])
                        distance = fam_start_num - fir_end_num
                        if distance < 4 and distance > 0:
                            with open("formatLink2.1_c3.txt", 'a',encoding='utf-8') as file:
                                file.write("ZJU\t" + alias +"\t" + filename +':'+str(fir_start_num)+'-'+str(fam_end_num)+ "\n")
                                word_nums = word_nums+1
    elif len(firfam) == 2 or len(firfam)==3: 
        if(B.exists(alias)): 
            allWordsUnNoun = len(firfam)
            for i in range(len(firfam)):
                if(D.exists(firfam[i].lower()) or C.exists(firfam[i].lower()) or firfam[i].isdigit()):
                    allWordsUnNoun -= 1
            if allWordsUnNoun == 0:
                continue 
            else:
                item = B.get(alias)
                with open("formatLink2.1_c3.txt", 'a',encoding='utf-8') as file:
                    #file.write(item[1])
                    for locations in item[0]:
                        file.write("ZJU\t" + item[1] +"\t" + locations+ "\n")
                        word_nums = word_nums+1
    elif len(firfam) == 1:  
        if(B.exists(alias) and not C.exists(alias.lower()) and not D.exists(alias.lower()) and not alias.isdigit()):
            if(alias[-1] == 's' and C.exists(alias[0:-1].lower())):
                continue
            else:
                item = B.get(alias)
                with open("formatLink2.1_c3.txt", 'a',encoding='utf-8') as file:
                    #file.write(item[1])
                    for locations in item[0]:
                        file.write("ZJU\t" + item[1] +"\t" + locations+ "\n")
                        word_nums = word_nums+1
#

print("word_nums: ", word_nums)
print(time.time()-start_time3)

print("totaltime: ", time.time()-start_time)
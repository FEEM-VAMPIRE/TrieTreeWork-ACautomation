import pickle


def isin(alias):
    if alias in aliasset:
        return True
    else: return False


aliasset= []
with open('../../ms_nam_mention.txt', 'r', encoding='utf-8') as file:
    for line in file:
        aliasset.append(line.rstrip('\n'))


ingoldnotinguessset = []

with open('ingoldnotinguess', 'r', encoding="utf-8") as file:
    for line in file:
        ingoldnotinguessset.append(line.rstrip('\n'))


for word in ingoldnotinguessset:
    if not isin(word):
        with open('ingoldnotinAlias', 'a', encoding="utf-8") as file:
            file.write(word+'\n')
    else :
        with open('ingoldinAliasnotinguess', 'a', encoding="utf-8") as file:
            file.write(word+'\n')


aliasset = []
totalword = 0
with open('ungetsetofchen', 'r', encoding='utf-8') as file:
    for line in file:
        aliasset.append(line.rstrip('\n'))
        totalword+=1

longword = 0
tribleword = 0
doubleword = 0
sigleword = 0
for word in aliasset:
    if len(word.split())>3:
        longword+=1
    elif len(word.split())==3:
        tribleword+=1
    elif len(word.split())==2:
        doubleword+=1
    else:
        sigleword+=1

print("totalword: ",totalword)
print("longword: ",longword)
print("tribleword: ",tribleword)
print("doubleword: ", doubleword)
print("sigleword: ",sigleword)
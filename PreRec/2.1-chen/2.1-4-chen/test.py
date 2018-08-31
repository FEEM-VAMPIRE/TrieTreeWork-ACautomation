ingoldnotinAlias=[]
with open('ingoldnotinAlias', 'r', encoding="utf-8") as file:
    for line in file:
        ingoldnotinAlias.append(line.rstrip('\n'))

lowerWordNum = 0
for word in ingoldnotinAlias:
    if word.lower()==word:
        lowerWordNum += 1

print(lowerWordNum)
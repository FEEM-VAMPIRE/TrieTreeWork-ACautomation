m = []
m.append((['ENG_DF_000354_20150626_G00A04NA1: 65', 'ENG_DF_000354_20150626_G00A04NA1: 101', 'ENG_DF_000354_20150626_G00A04NA1: 103', 'ENG_DF_000354_20150626_G00A04NA1: 155', 'ENG_DF_000354_20150626_G00A04NA1: 162', 'ENG_DF_000354_20150626_G00A04NA1: 988', 'ENG_DF_000354_20150626_G00A04NA1: 512', 'ENG_DF_000354_20150626_G00A04NA1: 68', 'ENG_DF_000354_20150626_G00A04NA1: 193', 'ENG_DF_000354_20150626_G00A04NA1: 518', 'ENG_DF_000354_20150626_G00A04NA1: 37', 'ENG_DF_000354_20150626_G00A04NA1: 107', 'ENG_DF_000354_20150626_G00A04NA1: 95', 'ENG_DF_000354_20150626_G00A04NA1: 129', 'ENG_DF_000354_20150626_G00A04NA1: 479', 'ENG_DF_000354_20150626_G00A04NA1: 84', 'ENG_DF_000354_20150626_G00A04NA1: 153', 'ENG_DF_000354_20150626_G00A04NA1: 232', 'ENG_DF_000354_20150626_G00A04NA1: 298', 'ENG_DF_000354_20150626_G00A04NA1: 604', 'ENG_DF_000354_20150626_G00A04NA1: 672', 'ENG_DF_000354_20150626_G00A04NA1: 695'], 'Senate'))
m.append((['ENG_DF_000354_20150626_G00A04NA1: 211', 'ENG_DF_000354_20150626_G00A04NA1: 712'], 'mklos'))
m.append((['ENG_DF_000354_20150626_G00A04NA1: 172', 'ENG_DF_000354_20150626_G00A04NA1: 174'], 'Christie'))

for item in m:
    print(item[1])
    for locations in item[0]:
        print("ZJU\t" + item[1] +"\t" + locations)

with open("result.txt", 'w') as file:
    for item in m:
        #file.write(item[1])
        for locations in item[0]:
            file.write("ZJU\r\t" + item[1] +"\r\t" + locations+ "\n")
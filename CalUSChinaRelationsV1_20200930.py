#CalUSChinaRelationsV1.py
def getText():
    txt =open("USChinaRelations.txt", "r", encoding = "utf-8").read()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt
    
USChinaTxt = getText()

excloudes = {"the","and","to","of","that","is","in","are","it","be","will","they","for",\
             "have","which","other","them","their","more","with","because","these","as","what",\
             "most","by","on","we","power","would","has","how","or","not","than","there","its",\
             "can","so","from","The","at","being","much","each","both","this","about","if","do","those","one","when"}

# 形成列表
words = USChinaTxt.split()    

# 将列表中元素变成字典键值对        
counts = {}
for word in words:
    if len(word)==1:
        continue
    elif word == "United States" or word == "US":
        rword ="US"
    
    else:
        rword = word        
    counts[rword]= counts.get(rword,0) + 1

for word in excloudes:
    del counts[word]


# 将键值对变成一个列表里的元组
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(30):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
        
    
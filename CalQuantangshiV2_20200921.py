#CalQuantangshiV2.py
import jieba

def getText():
    txt = open("quantangshi.txt", "r", encoding = "utf-8").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~1234567890]】【':
        txt = txt.replace(ch, " ")
    return txt


excloudes = {"何处","一作","万里","今日","二首","春风","白云","不知","千里","不可","长安","不见","国学","原典","集部","全唐诗","故人","无人","不得","明月","齐己","人间","惆怅","使君","秋风","悠悠","相思","如何","青山","白日","何人","相逢","皎然","江南","乐章","少年","寂寞","平生","黄金","司空","山中","何事","贯休"}
words = jieba.lcut(getText())
counts = {}

for word in words:
    if len(word)==1:
        continue
    else:
        rword = word        
    counts[rword]= counts.get(rword,0) + 1


for word in excloudes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
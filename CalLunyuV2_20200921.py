#CalLunyuV2.py
import jieba

jieba.add_word("子曰")
jieba.add_word("子见")
jieba.add_word("子闻")

txt = open("lunyu.txt", "r", encoding = "utf-8").read()
excloudes = {"君子","可以","仁者","何如","可谓","不知","小人","不可","不能","天下","三子","不足","而已","不如","无道","大夫","不食","问政","朋友","至于","与其","不得","弟子","三年","何以","以为","如之何","何有"}
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word)==1:
        continue
    elif word == "夫子" or word == "子谓" or word =="子曰" or word =="子见" or word=="子闻":
        rword ="孔子"
    elif word == "子贡曰":
        rword = "子贡"
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
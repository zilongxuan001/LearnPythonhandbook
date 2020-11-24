#CloudLunYuv1.py
import jieba
import wordcloud
from imageio import imread

mask = imread("kongzi.png")

f = open("lunyu.txt", "r", encoding = "utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud( font_path= "msyh.ttc", mask = mask, width = 1000, height = 700, background_color = "white")

w.generate(txt)
w.to_file("lunyu.png")
#  BianLiV1.py


fname = input("请输入要打开的文件名称：")
fo = open(fname, "r", encoding= "utf-8")
txt = fo.read(2)
# 对全文本txt进行处理
fo.close()
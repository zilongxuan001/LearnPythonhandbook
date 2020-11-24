# BianLiV2.py

fname = input("请输入要打开的文件名称：")
fo = open(fname, "r", encoding= "utf-8")
txt = fo.read(2)
txt = fo.seek(0,0)
while txt != "":
	txt = fo.read(2);print(txt)    
fo.close()

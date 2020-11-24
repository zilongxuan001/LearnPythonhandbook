# 引入argv模块
from sys import argv
# 将argv赋值给scirpt, filename
script, filename =  argv
# 打开filename,文件内容给txt
txt = open(filename)
# 打印一段话，读取txt的文件内容
print(f"Here's your file {filename}:")
print(txt.read())
#打印一段话，把文件名赋值给file_again
print("Type the filename again:")
file_again = input("> ")
# 打开file_again,把文件内容赋值给txt_again
txt_again = open(file_again)
# 读取txt_again的内容。
print(txt_again.read())
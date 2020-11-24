# 导入模块

from os.path import exists
from sys import argv

# argv赋值
script, from_file, to_file = argv

# 打印要从输入文件拷贝到输出文件
print(f"We will copy {from_file} to {to_file}  ")


# 打开文件，读取输出文件
target = open(from_file, encoding='utf-8', errors='ignore')

fileName = target.read()

# 检测输入文件内容长度大小

print(f"There have the {len(fileName)} bites in from_file.")

# 检测输出文件是否存在

print(f"Do the {to_file} exists?{exists(to_file)}")

# 询问是否继续复制
print(f"Do we continue to copy file? ")

print(input(""))

# 打开要输入文件，并写入文件

mainFile = open(to_file, "w")

mainFile.write(fileName)


# 关闭输出文件和输入文件
target.close()
mainFile.close()

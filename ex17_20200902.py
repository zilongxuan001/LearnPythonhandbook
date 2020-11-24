# 把一个文件拷贝到另一个文件

# 导入模块
from sys import argv
from os.path import exists

# argv赋值
srcipt, from_file, to_file = argv

# 打印要从输入文件拷贝到输出文件
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# 打开文件，读取输出文件
in_file = open(from_file, encoding='utf-8', errors='ignore')
indata = in_file.read()

# 检测输入文件内容长度大小
print(f"The input file is {len(indata)} bytes long")

# 检测输出文件是否存在
print(f"Does the output file exists? {exists(to_file)}")

# 询问是否继续复制
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# 打开要输入文件，并写入文件
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# 关闭输出文件和输入文件
out_file.close()
in_file.close()


# 导入argv
from sys import argv

# argv赋值文件
script, input_file = argv

# 定义读取文件和输出文件的函数
def print_all(f):
    print(f.read())
    
    
# 定义回到文件开始的函数    
def rewind(f):
    f.seek(0)

# 定义数字和输出每行的函数
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 打开文件 
current_file = open(input_file)

# 打印输出所有内容
print("First let's print the whole file: \n")

# 输出所有内容
print_all(current_file)

# 打印回到第一行
print("Now let's rewind, kind of like a tape.")

# 回到第一行
rewind(current_file)

# 打印输出每一行
print("Let's print three lines:")

# 赋值1给current_line,输出第1行
current_line = 1
print_a_line(current_line, current_file)

# 赋值+1给current_line,输出第2行
current_line += 1
print_a_line(current_line, current_file)

# 赋值+1给current_line,输出第3行
current_line += 1
print_a_line(current_line, current_file)


    
    
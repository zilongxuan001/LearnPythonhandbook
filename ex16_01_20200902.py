from sys import argv

script, filename = argv

print("Let's open the file:")


target= open(filename, 'r+')


print("Let's erase the content.")

target.truncate()

print("Let's write something")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("Let's close the file.")

target.close()

file= open(filename, 'r')

readFile = file.read()

# 游标移动到第一行，否则读取的是空。
file.seek(0,0)
readFileLine = file.readline()


print(readFile)
print(readFileLine)



# 在test.txt里写入文件

from sys import argv

srcipt, file = argv

write_file = open(file, "w")

write_file.seek(0,0)

# This is line 1 如果放在第13行，则在test.txt会空出第一行。
write_file.write("""This is line 1
This is line 2
This is line 3
""")

write_file.close()



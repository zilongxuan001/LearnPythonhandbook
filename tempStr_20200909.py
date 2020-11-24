# tempStr.py 温度转化器

# 打印一个输入函数，输入温度。
tmpStr = input("请输入带有符号的温度值：")

# 如果温度的倒数第一个字母是C或者c, 将其转化为华氏度
if tmpStr[-1] in ['C','c']:
    F = 1.8* eval(tmpStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))

# 如果温度的倒数第一个字母是F或者f, 将其转化为普通温度
elif tmpStr[-1] in ['F','f']:
    C = (eval(tmpStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))

# 如果两者皆不是，则输入你输入的格式有错误
else:
    print("你输入的格式有错误。")

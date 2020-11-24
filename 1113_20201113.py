# 获取用户不定长度的输入
def getNum():
    nums = [] 
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums


# 计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s +=num
    return s/len(numbers)

# 计算方差：
def dev(numbers,mean):
    sdev =0.0
    for num in numbers:
        sdev +=(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

# 计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size %2 ==0:
        med = (numbers[size//2 -1] +numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

# 执行函数
n= getNum()
m = mean(n)
print(f"平均值：{m}, 方差：{dev(n,m):.2}, 中位数：{median(n)}")

# 错误：
# 第37行：`m = mean()`缺少参数n，→`m=mean(n)`
# 第30行：`med = (numberss[size//2 -1] +numbers[size//2])/2`中numberss拼写错误，应为`numbers`

# 框架
# 功能块：获得数字，计算平均数，计算方差，计算中位数

# 使用工具
# def
# 空列表[]
# input()
# while
# list.append()
# eval()
# return
# for in 
# +=
# len()
# **
# pow()
# sorted()
# if...else...
# %
# ==
# print



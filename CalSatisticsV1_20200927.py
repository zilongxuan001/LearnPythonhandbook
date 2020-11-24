#CalSatisticsV1.py

# 获取用户不定长度的输入
def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）: ")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）： ")
    return nums

# 计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s +num
    return s /len(numbers)
 

# 计算方差

def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev +(num-mean)**2
    return pow(sdev/(len(numbers)-1), 0.5)
    

# 计算中位数

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size %2 ==0:
        med= (numbers[size//2 -1]+ numbers[size//2])/2
    else:
        med= numbers[size//2]
        
    return med

# 执行函数
n = getNum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数：{}.".format(m,dev(n,m),median(n)))




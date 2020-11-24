# 请在...补充一行或多行代码

def prime(m):
    if m < 2:  # 判断数字是否为1
        return False
    else:
        end = int(pow(m, 0.5) + 1)  
        for i in range(2, end):   # 判断是否为质数，质数为True
            if m%i == 0:
                return False
        else:
            return True

n = eval(input())
if n != int(n):     # 判断是否为整数
    n = int(n) + 1
else:  
    n = int(n)
count = 5
while count > 0:  
    if prime(n):
        if count > 1:   # 加上逗号
            print(n, end=',')
        else:           # 最后一个不加逗号
            print(n)
        count -= 1
    n += 1

# 判断数字是否为1
# 判断是否为质数，质数为True
# 判断是否为整数
# 打印数字，并加上逗号

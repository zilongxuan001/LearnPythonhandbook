# 获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬
# 注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。
# 几个功能块
# 判断数字是否小于2
# 判断是否为质数，质数为True
# 判断是否为整数
# 打印数字，并加上逗号

def prime(N):
    if N < 2:                   # 判断数字是为小于2，如果为2，则返回错误
        return False
    else:
        n = int(pow(N, 0.5) +1) # 求取平方根，减少运算次数。
        for i in range(2,n):    # 判断是否为质数。
            if N %i ==0:
                return False
        else:                   # 如果for循环执行完毕，则返回True。
            return True
num =eval(input())              # 输入数字
if num != int(num):             # 判断是否为整数，如果不是，则+1
    num =int(num)+1
else:
    num = int(num)              
count =5
while count >0:
    if prime(num):              # if如果为True,则为质数，执行下面语句
        if count >1:            # 如果为前4个数，则在后面加逗号。
            print(num, end=',')
        else:                   
            print(num)          # 如果是第五个数，则不加逗号。
        count -=1
    num +=1


        
# 第一行`if N ==1:`错误，应为'if N < 2:'
# 第26行到第32行，判断打印数据错误，
# if Prime(num) ==False:
#         num +=1
#         Prime(Num)
#     else:
#         print(num, end=",")
#         count -=1
#         if count >1:
#             print(num)
# 结构功能不清。
# 第21行 `num +=+1`错误，应为`num =int(num)+1
# 第17,18行错误，else应该和for处于同一层级。
# 
# for else语句应用相当精妙，当for循环正常完成时，就执行else语句。




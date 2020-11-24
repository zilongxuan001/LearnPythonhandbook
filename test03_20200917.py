# test03.py 
# trans Celsius and Fahrenheit

temp = input("请输入带字符的温度数值：")

if temp[-1] in ["C", "c"]:
    transTemp = eval(temp[0:-1]) * 1.8 +32
    print("{:.2f}F".format(transTemp))
elif temp[-1] in ["F","f"]:
    transTemp = (eval(temp[0:-1])-32)/1.8
    print("{:.2f}C".format(transTemp))
else:
    print("输入格式错误。")
    
    


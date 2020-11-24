# transMoney

money = input("请输入带RMB或USD符号的货币：")

if money[0]in ["R","r"]:
    
    usd = eval(money[3:])/6.78
    print("USD{:.2f}".format(usd))
elif money[0] in ["u",'U']:
    rmb = eval(money[3:]) * 6.78
    print("RMBd{:.2f}".format(rmb))
    
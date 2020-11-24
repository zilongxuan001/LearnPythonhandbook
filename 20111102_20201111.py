class Product():
    def __init__(self,name): # 定义类对象的变量
        self.name = name     # 定义类对象的name变量
        self.label_price = 0 # 定义类对象的labe_price变量
        self.real_price = 0  # 定义类对象的real_price变量

c = Product("电脑")  # 建立实例
d = Product("打印机") # 建立实例
e = Product("投影仪") # 建立实例

c.label_price,c.real_price = 10000, 8000  # 赋予实例变量数值
d.label_price, d.label_price = 2000, 1000
e.label_price, e.label_price = 1500, 900
s1,s2=0,0

for i in [c ,d ,e]:  # 通过for  in 将数量累加
    s1 += i.real_price
    s2 += i.label_price
print(s1,s2)

# 第2行 `def __init__:`错误，应为`def __init__(self,name):` 
# 第3行`self.name = 0`错误，应为`self.name = name`
#  第12行`d.label_price, d.label_price = 2000，1000`中的`2000，1000`逗号错误，应为英文逗号
# 
# 框架
# 这是使用class的一个实例，首先定义了“Product”这个类，建立对象。
# 然后添加标签价和实际价，通过for...in将3种商品的标签价和实际价分别加起来。


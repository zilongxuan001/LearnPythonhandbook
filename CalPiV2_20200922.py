#CalPiV2.py

# 引入random库和time库
from random import random
from time import perf_counter
# 设置值一共1000*1000个灰尘，落入灰尘设为初始值0，设置开始时间。
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
# 随机落入灰尘，根据直角公式求第三边也就是灰尘到圆心的距离，距离小于1则在圆内，距离大于1则在圆外。叠加在圆内的灰尘。
#圆的直径是1，则圆面积就是π。

for i in range(1,DARTS+1):
    x, y =random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <=1.0:
      hits = hits + 1

# 因为算的是1/4的面积，所以算所有的圆面积，则乘以4      
pi = 4 * (hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))

    
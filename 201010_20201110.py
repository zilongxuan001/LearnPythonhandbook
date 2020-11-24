count=0
def hanoi(n,src, dst, mid):
    global count
    if n == 1:
        print(f"{1}:{src}->{dst}")
        count+=1
    else:
        hanoi(n-1,src,mid,dst)       #第一步：n-1阶从A→B
        print(f"{n}:{src}->{dst}")   #第二步：第n个从A→C
        count+=1
        hanoi(n-1,mid,dst,src)       # 第三步：n-1阶从B→C
    

def main():
    n = eval(input("请输入阶数："))
    hanoi(n, "A","C","B")
    print(count)
    
main()

# 原理：
# 汉诺塔是典型的函数递归应用的案例，不能简单的用2阶汉诺塔、3阶汉诺塔推理至n阶汉诺塔的方式去理解，必须站在n和n-1的关系去理解。
# 有三个柱子A、B、C,有n阶汉诺塔，从递归的角度考虑，把汉诺塔分为第n个和n-1阶
# 第一步：n-1阶从A→B
# 第二步：第n个从A→C
# 第三步：n-1阶从B→C  
# 
# 自己感悟
# 汉诺塔虽然理解上有些难，但只要多给点时间，还是能够想通的。
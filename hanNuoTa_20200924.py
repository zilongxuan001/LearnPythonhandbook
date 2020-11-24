# hanNuoTa.py

count = 0
def hanoi(n,src, dst, mid): #定义源柱子，目标柱子，中间柱子
    global count
    if n ==1:
        print("{}:{}->{}".format(1,src,dst))
        count +=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
        
hanoi(3,"A","C","B")
print(count)
       
        

sum =0
for i in range(2,101):
    for b in range(2,i):
        if i%b == 0:
            break
        else:
            sum += i
print(sum)
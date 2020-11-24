# pyramid

import turtle as t

t.pencolor("gold")
t.pensize(2)

count = 10

while count > 0:
    for i in range(count):
        t.fd(10)
        for j in range(4):
            t.left(90)
            t.fd(10)  
    t.fd(-(count*10))
    t.left(90)
    t.fd(10)
    t.right(90)
    t.fd(5)
    count -=1
        
 
t.done()

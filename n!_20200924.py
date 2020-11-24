# n!.py

import turtle

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=1


while n < 6:
    turtle.circle(fact(n))
    n+=1


turtle.done()
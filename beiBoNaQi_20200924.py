# beiBoNaQi.py
import turtle

def  f(n):
	if n ==1 or n ==2:
		return 1
	else:
		return f(n-1) + f(n-2)
        
n=1

while n < 20:
    turtle.circle(f(n))
    n+=1


turtle.done()
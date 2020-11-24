# KochDrawV3.py
# 科赫多个雪花

import turtle
def koch(size,n):
    if n ==0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
turtle.setup(600, 600)

def main():
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("green")
    level =3
    koch(40, level)
    turtle.right(120)
    koch(40,level)
    turtle.right(120)
    koch(40,level)
    turtle.penup()
    turtle.fd(80)
    
    
    
i=1

while i <5:
    main()
    i+=1

turtle.hideturtle()
turtle.done()
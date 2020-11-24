# happyFace.py

import turtle
turtle.circle(40, 360)

turtle.color("green")

turtle.penup()
turtle.left(90)
turtle.fd(50)
turtle.left(-90)
turtle.fd(20)
turtle.pendown()

turtle.begin_fill()
turtle.circle(5, 360)
turtle.end_fill()

turtle.penup()
turtle.bk(40)

turtle.pendown()

turtle.begin_fill()
turtle.circle(5, 360)
turtle.end_fill()

turtle.penup()
turtle.fd(20)

turtle.right(90)

turtle.fd(15)

turtle.right(90)

turtle.fd(20)

turtle.right(-90)

turtle.pendown()


turtle.circle(20, 180)



turtle.done() 
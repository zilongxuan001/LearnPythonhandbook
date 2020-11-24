# bear
import turtle as t

# 脸

t.pensize(2)
t.color('yellow')
t.pencolor("black")
t.begin_fill()
t.circle(40,360)

# 右耳朵
t.circle(40,135)
t.left(-90)
t.circle(10, 200)
t.end_fill()

# 左耳朵
t.penup()
t.goto(0,0)
t.seth(0)
t.pendown()
t.circle(40,225)
t.begin_fill()
t.right(90)
t.circle(-10, 200)
t.end_fill()

# 右眼睛框
t.penup()
t.goto(0,0)
t.seth(0)
t.left(90)
t.fd(50)
t.right(90)
t.fd(10)
t.pendown()
t.begin_fill()
t.circle(7, 360)
t.end_fill()

# 右眼睛瞳孔
t.penup()
t.left(90)
t.fd(5.5)
t.right(90)
t.fd(2)
t.left(-90)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(-3,360)
t.end_fill()


# 左眼眶
t.color('yellow')
t.pencolor("black")
t.penup()
t.goto(0,0)
t.seth(0)
t.left(90)
t.fd(50)
t.left(90)
t.fd(10)
t.pendown()
t.begin_fill()
t.circle(-7, 360)
t.end_fill()

# 左眼睛瞳孔
t.penup()
t.left(90)
t.fd(-5.5)
t.right(90)
t.fd(2)
t.left(-90)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(-3,360)
t.end_fill()

# 鼻子

t.penup()
t.goto(0,0)
t.seth(0)
t.left(90)
t.fd(35)
t.right(90)
t.pendown()
t.begin_fill()
t.circle(5,360)
t.end_fill()

# 嘴巴

t.penup()
t.goto(0,0)
t.seth(0)
t.left(90)
t.fd(20)
t.right(90)
t.fd(-10)
t.right(90)
t.pendown()
t.begin_fill()
t.circle(10,180)
t.end_fill()



t.hideturtle()

t.done()
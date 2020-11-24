#dramPozi.py
import turtle
import math

def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine():   #绘制最短横线
    drawGap()
    for i in range(2):
        turtle.pendown()
        turtle.fd(20)
        drawGap()
    turtle.right(90)

    drawGap()
    turtle.pendown()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
 
def drawLine2():   #绘制次短横线
    drawGap()
    turtle.pendown()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
def drawMi(): #绘制米字
    turtle.penup()
    turtle.fd(27.5)
    turtle.pendown()
    c = pow(27.5*27.5+50*50, 0.5)
    a = 27.5
    b = 50
    d = c-5
    angle= 90-math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
    turtle.right(angle)
    turtle.fd(d)
    turtle.fd(-d)
    turtle.right(-angle)
    turtle.right(-angle)
    turtle.fd(d)
    turtle.fd(-d)
    turtle.right(angle)
    turtle.right(180)
    turtle.right(-angle)
    turtle.fd(d)
    turtle.fd(-d)
    turtle.right(angle)
    turtle.right(angle)
    turtle.fd(d)
    turtle.fd(-d)
    turtle.right(-angle)
    turtle.penup()
    turtle.fd(27.5)
    
    
    
    
def drawPozi(): #画灰色米字方框
    turtle.pencolor("gray")
    drawLine()
    drawLine()
    turtle.left(90)
    drawLine2()
    drawLine()
    drawMi()
 
drawPozi()  
turtle.done()  
    
    
    
    
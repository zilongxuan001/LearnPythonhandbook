import turtle,time,math

def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine3():   #绘制米字最短横线
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
    
drawLine3()

turtle.done()
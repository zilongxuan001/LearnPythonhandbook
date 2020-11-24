# PoziCubeDigitalV2.py

# 代码有问题，米字管右边不能完全重合，应该是设计问题。

import turtle,time,math

def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):   #绘制最短横线
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(20)
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(20)
    turtle.right(90)
    
def drawLine2(draw):   #绘制次短横线
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
  
def drawDigit(digit): #根据数字绘制七段数码管，最好自己将10个数字用七段数码管画一下，这样比较好理解。
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)   # 中间一横
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False) # 右边下方的一竖
    drawLine2(True) if digit in [0,2,3,5,6,8,9] else drawLine2(False)   # 最下边一横
    
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)         # 左边下方的一竖
    
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)     # 左边上方的一竖
    drawLine2(True) if digit in [0,2,3,5,6,7,8,9] else drawLine2(False)  # 最上边的一横
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)  # 右边上方的一竖

    turtle.left(180)
    turtle.penup()  # 为绘制后续数字确定位置
    turtle.fd(20)   # 为绘制后续数字确定位置

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
    
def drawLine4():   #绘制米字次短横线
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
    drawLine3()
    drawLine3()
    turtle.left(90)
    drawLine4()
    drawLine3()
    drawMi()

def drawDate(date):    #获得要输出的数字,date为日期，格式为'%Y-%m=%d+'
    for i in date:
        if i == "-":
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "+":
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawPozi()
            turtle.fd(-55)
            turtle.pencolor("green")
            drawDigit(eval(i))
            
                    
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done() 
    
main()

# CountDown.py

import turtle,time

def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
  
def drawDigit(digit): #根据数字绘制七段数码管，最好自己将10个数字用七段数码管画一下，这样比较好理解。
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)   # 中间一横
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False) # 右边下方的一竖
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)   # 最下边一横
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)         # 左边下方的一竖
    
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)     # 左边上方的一竖
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)  # 最上边的一横
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)  # 右边上方的一竖

    

def drawDate():   
    turtle.pencolor("red")
    i=9
    while i>=0 :
        drawDigit(i)
        turtle.pencolor("white")
        drawDigit(8)
        turtle.pencolor("red")
        i-=1
    
            
                    
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate()
    turtle.hideturtle()
    turtle.done() 
    
main()
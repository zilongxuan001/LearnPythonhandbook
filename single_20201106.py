import turtle,time


def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawLine(draw): # 处理单个行
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit): # 处理单个字符
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)

    turtle.left(90) # 从中间一横开始，画4个横后，就需要直着前进一部分。
    drawLine(True) if digit in [0,4,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)

    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date): # 将日期分解为单个字符。
    turtle.pencolor("red") 
    for i in date: # 循环取出每个数字
        if i == "-":
            turtle.write('年', font=("Arial",18,"bold"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write('月', font=("Arail",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "+":
            turtle.write('日', font=('Arail',18,'italic'))
        else:
            drawDigit(eval(i))

def main(): # 建设画布，获得日期
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.speed(100)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()

#犯的错误：
#1. 第31行turtle.pencolor("red") 多了':'，修改方法：去掉':'
#2. 第34、38、42行的font前的“，”错了，为中文标号，改成英文","
#3. 第26行“turle.left(180)”拼写错了，改为“turtle.left(180)”
#4. 第18行“drawLine(True) if digit in [0,2,3,5,6,8,9] else drawline(False)”的“drawline”拼写错误，应为“drawLine”

# 原理：
# 7段数码管是个8字形，每次海龟画线都从中间一段横线开始，不断右转，或直线，每段横线画出线，或者不画出线。
# 
# main()控制所有函数：
# 1.设置画布大小，并移动海龟到合适位置。
# 2.其次设置笔触大小
# 3.根据时间画七段管。设置时间显示的格式，并获得时间，调用drawDate()函数，根据时间格式画七段管。
# 4.隐藏海龟，并在画布上停留。
#
# drawDate()控制所有日期：
# 1.根据时间的格式区分出“年”、“月”、“日”，设置颜色，并写出来，再右移动。
# 2.drawDigit()写年月日的数字。
# 
# drawDigit()中控制单个数字：
# 1. 调用drawLine()，根据每个数字的不同，画出每个数字来。
# 2. 画完每个数字后，调整方向，并右移一段时间。
# 
# drawLine()中控制每一横：
# 1. 调用drawGap()形成横与横之间的缝隙
# 2. 根据drawDigit()控制海龟是否抬起还放下。
# 3. 画横。如果海龟抬起，则无痕迹，如果海龟放下，则留下一横。
# 4. 调用drawGap()形成横与横之间的缝隙
# 5. 右转90度。

# 点评：
# 该代码的函数环环相套，从获得日期，循环取出，分解为单个字符，最后具体到每一横。是自顶向下设计，分解目标

# 新学内容：
# 单行写if...else行数，格式  <执行命令> if <判断条件> else <执行命令>
# turtle.pendown() if draw else turtle.penup() 
#
# 海龟直接写文字，turtle.write(),通过font()调整文字的字体，大小和正常（normal, 加粗Bold,斜体italic）
# turtle.write('年', font=("Arial",18,"normal"))  
  





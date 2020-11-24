# circles

import turtle as t

t.pencolor("pink")
t.left(90)
def main():

    for i in range(10):
        t.circle(10,360)
        t.penup()
        t.fd(20)
        t.pendown()
        
    t.penup()
    t.right(180)
    t.fd(200)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.pendown()

for i in range(10):
    main()

t.done()

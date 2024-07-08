import turtle

myPen = turtle.Turtle()


def square():
    for i in range(0, 4):
        myPen.forward(100)
        myPen.left(90)


def gap():
    myPen.penup()
    myPen.right(90)
    myPen.forward(50)
    myPen.pendown()


myPen.goto(-100, 0)

for i in range(4):
    square()
    myPen.penup()
    myPen.right(90)
    myPen.pendown()
    gap()
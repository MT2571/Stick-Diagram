# Turtle script example
import turtle
def nMOS1():
    t.speed(10)
    t.width(1)
    t.color('red')
    t.left(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write("A", font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(0, t.ycor() - 50)
    t.left(90)
    t.pendown
    
    
def exp_AandB():
    t.speed(10)
    t.width(1)
    t.color('red')
    t.left(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write("A", font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(100)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write("C", font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(0, t.ycor() - 50)
    t.left(90)
    t.pendown()
    
    
t = turtle.Turtle('turtle')
a = input()
ls = []
ls1 = ['(', 'a', '*', 'b', ')']
ls2 = ['+', 'c']
for i in a:
    ls.append(i)
    if (ls == ls1):
        exp_AandB()
        ls.clear()   
    if (ls == ls2):
        nMOS1()
print(ls)
print(ls1)
if (a == "AB"):
    exp_AandB()
turtle.done()


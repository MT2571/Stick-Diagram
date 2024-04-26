# Turtle script example
import re
import turtle
def draw_A(str):
    t.speed(5)
    t.width(1)
    t.color('red')
    t.left(90)
    t.forward(50)
    ls_heads.append(t.pos())
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write(str[1].upper(), font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(50)
    t.right(90)
    t.forward(50)
    ls_tails.append(t.pos())
    t.penup()
    t.goto(0, t.ycor() - 50)
    t.left(90)
    t.pendown()
    
    
def draw_AandB(str):
    t.speed(5)
    t.width(1)
    t.color('red')
    t.left(90)
    t.forward(50)
    ls_heads.append(t.pos())
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write(str[1].upper(), font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(100)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write(str[3].upper(), font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(50)
    t.right(90)
    t.forward(50)
    ls_tails.append(t.pos())
    t.penup()
    t.goto(0, t.ycor() - 50)
    t.left(90)
    t.pendown()
    
def draw_AorB(str):
    t.speed(5)
    t.width(1)
    t.color('red')
    t.left(90)
    t.forward(50)
    ls_heads.append(t.pos())
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.write("D", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write(str[1].upper(), font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("S", font=("Arial", 15, "normal"))
    t.forward(50)
    t.right(90)
    t.forward(50)
    ls_tails.append(t.pos())
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.write("S", align="right", font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(25)
    t.write(str[3].upper(), font=("Arial", 15, "normal"))
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.write("D", font=("Arial", 15, "normal"))
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.penup()
    t.goto(0, t.ycor() - 150)
    t.left(90)
    t.left(90)
    t.pendown()

def connect_2cor(x, y):
    r = turtle.Turtle()
    r.penup()
    r.goto(x)
    r.pendown()
    r.goto(y)
    r.hideturtle()

def format_A_and_B(str):
    if (len(str) == 5 and str[2] == '*'):
        return True
    return False
def format_A_or_B(str):
    if (len(str) == 5 and str[2] == '+'):
        return True
    return False
def format_A(str):
    if (len(str) == 3 and str[1].isalpha()):
        return True
    return False

t = turtle.Turtle()
ls_heads = []
ls_tails = []
pattern_AandB = re.compile(r'^(.*.)$')
y = input("Enter an expression")
print(y)
ls = []
for i in y:
    ls.append(i)
    if (i == ')'):
        j = len(ls) - 1
        str = ""
        while (ls[j] != '('):
            str += ls.pop()
            j -= 1
        str += ls.pop()
        str = "".join(reversed(str))
        print("str" + str)
        if (format_A_and_B(str)):
            draw_AandB(str)
        if (format_A_or_B(str)):
            draw_AorB(str)
        if (format_A(str)):
            draw_A(str)
        if (str == "(+)"):
            connect_2cor(ls_heads[-1], ls_heads[-2])
            connect_2cor(ls_tails[-1], ls_tails[-2])
            ls_heads.pop(1)
            ls_tails.pop(0)
        if (str == "(*)"):
            connect_2cor(ls_tails[0], ls_heads[1])
            ls_heads.pop(1)
            ls_tails.pop(0)
print(ls)
print(ls_heads)
print(ls_tails)
turtle.done()




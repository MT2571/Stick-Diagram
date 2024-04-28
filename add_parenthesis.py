y = "(a*b)+(c*d)+(a+b)*(e)"
def add_parenthesis(y):
    index = y.find(")*(")
    while (index != -1):
        y = y[:index+1] + 'x' + y[index+2:]
        stack = []
        for i in range(index, -1, -1):
            if (y[i] == ")"):
                print("Hello")
                stack.append(i)
            elif (y[i] == "(" and len(stack) == 1):
                y = y[0:i] + '(' + y[i:]
                print("I'm here")
                stack.pop()
                break;
            elif (y[i] == "("):
                stack.pop()
        
        for i in range(index+2, len(y)):
            if (y[i] == "("):
                print("Hello")
                stack.append(i)
            elif (y[i] == ")" and len(stack) == 1):
                y = y[0:i] + ')' + y[i:]
                print("I'm here")
                stack.pop()
                break;
            elif (y[i] == ")"):
                stack.pop()
        index = y.find(")*(")
        
    index = y.find(")+(")
    while (index != -1):
        y = y[:index+1] + '~' + y[index+2:]
        stack = []
        for i in range(index, -1, -1):
            if (y[i] == ")"):
                print("Hello")
                stack.append(i)
            elif (y[i] == "(" and len(stack) == 1):
                y = y[0:i] + '(' + y[i:]
                print("I'm here")
                stack.pop()
                break;
            elif (y[i] == "("):
                stack.pop()
        
        for i in range(index+2, len(y)):
            if (y[i] == "("):
                print("Hello")
                stack.append(i)
            elif (y[i] == ")" and len(stack) == 1):
                y = y[0:i] + ')' + y[i:]
                print("I'm here")
                stack.pop()
                break;
            elif (y[i] == ")"):
                stack.pop()
        index = y.find(")+(")
    y = y.replace("x", "*")
    y = y.replace("~", "+")
    return y
y = add_parenthesis(y)
print(y)

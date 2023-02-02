'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.
'''


def evalRPN(tokens):
    operators = ["+", "-", "*", "/"]
    stack = []

    for i in range(len(tokens)):

        if tokens[i] in operators:
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
                # print(stack)
            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
                # print(stack)
            elif tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
               # print(stack)
            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
                # print(stack)
        else:
            stack.append(int(tokens[i]))
            # print(stack)

    return stack[0]

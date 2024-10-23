# 1

operator = input("Input operator (+, -, *, /): ")

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

operators  = ["+","-","*","/"]

def calculator():
    if operator == operators[0]:
        return number1 + number2
    if operator == operators[1]:
        return number1 - number2
    if operator == operators[2]:
        return number1 * number2
    if operator == operators[3]:
        return number1 / number2

res = calculator()
print(res)


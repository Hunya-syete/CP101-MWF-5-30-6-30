calculator = input("enter an operator (+ - * /): ")
num1 = (input("Enter the 1st number: "))
num2 = (input("Enter the 2nd number: "))

if calculator == "+":
    result = num1 + num2
    print(result)
elif calculator == "-":
    result = num1 - num2
    print(result)
elif calculator == "*":
    result = num1 * num2
    print(result)
elif calculator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{calculator} is not a valid operator")

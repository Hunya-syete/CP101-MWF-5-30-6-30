# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the operator from the user
op = input("Enter operator (+, -, *, /): ")

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the operator
if op == "+":
  result = num1 + num2
elif op == "-":
  result = num1 - num2
elif op == "*":
  result = num1 * num2
elif op == "/":
  if num2 == 0:
    result = "Division by zero is not allowed!"
  else:
    result = num1 / num2
else:
  result = "Invalid operator!"

# Print the result
print(result)

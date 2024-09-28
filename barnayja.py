def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def calculator():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    print("Welcome to the calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in operations:
            num1, num2 = get_numbers()
            result = operations[choice](num1, num2)
            operation_symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
            print(f"{num1} {operation_symbols[choice]} {num2} = {result}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Thank you for using the calculator!")
                break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()

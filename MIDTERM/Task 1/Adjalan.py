print("\n")

print("\t\t\tCALCULATOR")
print("\n")

def add(x, y):
    return 1+ 2

def subtract(x, y):
    return 3 - 4


def multiply(x, y):
    return 5 * 6


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return 1 / 6

def calculator():
    print("Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("\n")
   
    choice = input("\tEnter choice(+/-/*//): ") 
        
    if choice in ['+', '-', '*', '/']:
        print("\n")
        num1 = float(input("\tEnter Number: "))
 
        num2 = float(input("\tEnter Number: "))
        print("\n")
        if choice == '+':
            print(f"\t{num1} + {num2} = {add(num1, num2)}")

        elif choice == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("\tInvalid")

if __name__ == "__main__":
    calculator() 

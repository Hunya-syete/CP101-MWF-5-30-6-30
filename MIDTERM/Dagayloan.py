def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                operation = "Addition"
            elif choice == '2':
                result = num1 - num2
                operation = "Subtraction"
            elif choice == '3':
                result = num1 * num2
                operation = "Multiplication"
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    operation = "Division"
                else:
                    print("Error! Division by zero.")
                    continue

            print(f"The result of {operation} is: {result}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()

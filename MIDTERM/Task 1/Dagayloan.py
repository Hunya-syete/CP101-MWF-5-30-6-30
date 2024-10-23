class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def run(self):
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
                    print(f"{num1} + {num2} = {self.add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {self.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {self.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {self.divide(num1, num2)}")
            else:
                print("Invalid input")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
                                   

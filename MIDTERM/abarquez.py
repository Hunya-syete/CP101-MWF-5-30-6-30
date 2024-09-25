# Calculator App

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return 'Cannot divide by zero'
        return x / y

# Example of using the Calculator
my_calculator = Calculator()

# Perform operations
print('Addition:', my_calculator.add(5, 3))
print('Subtraction:', my_calculator.subtract(5, 3))
print('Multiplication:', my_calculator.multiply(5, 3))
print('Division:', my_calculator.divide(6, 2))

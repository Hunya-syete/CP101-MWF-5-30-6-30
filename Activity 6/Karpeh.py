# Part 1: Basic f-string Formatting

# Prompt the user for their name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# Display the name and age using f-string formatting
print(f"Hello, {name}! You are {age} years old.")


# Part 2: Using .format()

# Example: Display a table of items and prices using .format()
items = ["Bread", "Milk", "Eggs", "Cheese"]
prices = [1.50, 0.99, 2.50, 3.75]

# Print the table header with aligned columns
print("\n{:<10} {:>10}".format("Item", "Price"))

# Print each item and price, aligned using .format() method
for item, price in zip(items, prices):
    print("{:<10} ${:>8.2f}".format(item, price))
    

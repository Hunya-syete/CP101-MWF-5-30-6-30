# Create a Python code that solves the following exercises by applying the appropriate string formatting method:

# Part 1: Basic f-string Formatting 
# Prompt the user for input and display it using f-strings. 
# Example: Display a name and age.

# Part 2: Using  .format() 
# Format strings dynamically with the .format() method.
# Example: Align items and prices in a table.

# Part 3: Legacy % formatting.
# Use the % formatting for displaying a string.
# Example: Display a message with a temperature value.




name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello, {name}! You are {age} years old.")


item = "apples"
count = 5
# Use the .format() method
sentence = "I bought {} {} today.".format(count, item)
print(sentence)


city = "New York"
temperature = 22
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))

# PART 1


name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! You are {age} years old.")


# PART 2


item1 = "apples"
price1 = 1.99
item2 = "bananas"
price2 = 0.99
item3 = "cherries"
price3 = 2.99

print("{:<10} {:>10}".format("Item", "Price"))
print("{:<10} {:>10.2f}".format(item1, price1))
print("{:<10} {:>10.2f}".format(item2, price2))
print("{:<10} {:>10.2f}".format(item3, price3))


# PART 3


city = "New York"
temperature = 22

print("The temperature in %s is %d degrees Celsius." % (city, temperature))

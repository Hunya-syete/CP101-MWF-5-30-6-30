fname = input("Enter your firstname: ")
age = input("Enter your age: ")
print(f"Hello, {fname}! You are {age} years old.")

count = 3
item = "water bottle"
sentence = "I drank {} ammount of {} today!".format(count, item)
print(sentence)

city = "cebu city"
temperature = 37.8
print("The temperature in %s is %.1f degrees Celsius." % (city, temperature))

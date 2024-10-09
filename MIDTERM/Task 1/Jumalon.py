print ("""
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION""")
print("****************************************")
text = int(input("CHOOSE NUMBER ABOVE: "))

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

if text == 1:
    add = num1 + num2
    print("ANSWER: ", add)
    
elif text == 2:
    subtract = num1 - num2
    print("ANSWER: ", subtract)
    
elif text == 3:
    multiply = num1 * num2
    print("ANSWER: ", multiply)
    
elif text == 4:
    divide = num1 / num2
    print("ANSWER: ", divide)
    
else:
    print("Enter Correct Number")

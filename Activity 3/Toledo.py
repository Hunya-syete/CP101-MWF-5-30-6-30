@@ -0,0 +1,14 @@
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
# Prompt the user for hours worked
hours = float(input("Enter Hours: "))

# Prompt the user for rate per hour
rate = float(input("Enter Rate: "))

# Calculate gross pay
pay = hours * rate

# Display the result
print("Pay: {:.2f}".format(pay))

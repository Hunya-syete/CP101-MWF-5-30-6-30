# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = 35
rate = 2.75

hours = float(input("hours worked: "))
rate = float(input("rate per hour: "))
gross_pay = (hours * rate)
print(gross_pay)

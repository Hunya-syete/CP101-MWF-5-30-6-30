# Rustom Carl M. Valdez BSIT (5:30 - 6:30)

Years = int(input("Enter the Number of Years in service: "))
Department  = input("Enter the Department (IT, ACCT, HR): ").upper()

if Department == "IT" and Years >= 10:
    Salary = 10000
elif Department == "IT" and Years < 10:
    Salary = 5000
elif Department == "ACCT" and Years >= 10:
    Salary = 12000
elif Department == "ACCT" and Years < 10:
    Salary = 6000
elif Department == "HR" and Years >= 10:
    Salary = 15000 
elif Department == "HR"and Years < 10:
    Salary = 7500

print(f"The Salary for {Department.upper()} Department with {Years} Years of service is: {Salary}")

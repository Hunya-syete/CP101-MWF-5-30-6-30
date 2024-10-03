print("<EMPLOYEES SERVICES>")

print("\n")
office = str(input("Enter Office: "))
years = int(input("Enter Years In Service: "))

if years >= 10:
    
    if office.upper() == "IT":
        print(f"AMOUNT IN YEARS: 10000") 
    elif office.upper() == "ACCT":
        print(f"AMOUNT IN YEARS: 12000")
    elif office.upper() == "HR":
        print(f"AMOUNT IN YEARS: 15000")
else:
    if office.upper() == "IT":
        print(f"AMOUNT IN YEARS: 5000")
    elif office.upper() == "ACCT":
        print(f"AMOUNT IN YEARS: 6000")
    elif office.upper() == "HR":
        print(f"AMOUNT IN YEARS: 7500")

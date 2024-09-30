print()
print ("\t YEARS OF SERVICE IN PYTHON")
print()
years = int(input("Enter years of service: "))
office = str(input("Enter office: "))

if years >= 10:
    if office.upper() == "IT":
        print (f"Amount Given: 10000")
    elif office.upper() == "ACCT":
        print (f"Amount Given: 12000")
    elif office.upper() == "HR":
        print (f"Amount Given: 15000")

elif years < 10:
    if office.upper() == "IT":
        print (f"Amount Given: 5000")
    elif office.upper() == "ACCT":
        print (f"Amount Given: 6000")
    elif office.upper() == "HR":
        print (f"Amount Given: 7000")
        
print()
print ("END OF PROGRAM")

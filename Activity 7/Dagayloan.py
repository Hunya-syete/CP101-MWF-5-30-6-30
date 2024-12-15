def Calculate_Salary (office, years_of_service):
    if office == "IT":
        if years_of_service >= 10:
            return 10000
        else:
            return 5000
    elif office == "Accounting":
        if years_of_service >= 10:
            return 12000
        else:
            return 6000
    elif office == "HR":
        if years_of_service >= 10:
            return 15000
        else:
            return 7500
    else:
        salary = None
        print("Invalid Office.")

office = input("Enter the employee's office (IT, Accounting, HR): ")
years = int(input("Enter the number of years in service: "))

salary = Calculate_Salary(office, years)
print(f"The employee's salary is: {salary}") a

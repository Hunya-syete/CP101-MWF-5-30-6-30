def calculate_salary(years_in_service, office):
    
    salary = 0
    if years_in_service >= 10:
        if office == 'it':
            salary = 10000
        elif office == 'acct':
            salary = 12000
        elif office == 'hr':
            salary = 15000
    else:
        if office == 'it':
            salary = 5000
        elif office == 'acct':
            salary = 6000
        elif office == 'hr':
            salary = 7500
    return salary

def main():
   
    years_in_service = int(input("Enter the number of years in service: "))
    office = input("Enter the office (it, acct, hr): ").lower()

    
    salary = calculate_salary(years_in_service, office)

    if salary > 0:
        print(f"The salary for an employee with {years_in_service} years in {office} is: ${salary}")
    else:
        print("Invalid office type entered. Please enter 'it', 'acct', or 'hr'.")

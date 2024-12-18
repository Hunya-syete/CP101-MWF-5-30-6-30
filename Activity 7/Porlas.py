def calculate_salary(years_in_service, office):
    return salary

def main():
   
    years_in_service = int(input("Enter the number of years in service: "))
    office = input("Enter the office (it, acct, hr): ").lower()

    
    salary = calculate_salary(years_in_service, office)

    if salary > 0:
        print(f"The salary for an employee with {years_in_service} years in {office} is: ${salary}")
    else:
        print("Invalid office type entered. Please enter 'it', 'acct', or 'hr'.")

if __name__ == "__main__":
    main()

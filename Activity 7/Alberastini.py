def get_salary(years, office):
    if office == 'it':
        return 10000 if years >= 10 else 5000
    elif office == 'acct':
        return 12000 if years >= 10 else 6000
    elif office == 'hr':
        return 15000 if years >= 10 else 7500
    else:
        return None

def main():
    years = int(input("Enter the number of years in service: "))
    office = input("Enter the office (it, acct, hr): ").lower()

    salary = get_salary(years, office)

    if salary is not None:
        print(f"The salary for {years} years in the {office} office is: ${salary}")
    else:
        print("Invalid office entered. Please enter 'it', 'acct', or 'hr'.")

if __name__ == "__main__":
    main()

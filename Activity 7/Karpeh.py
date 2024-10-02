def calculate_bonus(years_in_service, office):
    if office.lower() == "hr":
        if years_in_service >= 10:
            return 30000
        else:
            return 5000
    elif office.lower() == "it":
        if years_in_service >= 10:
            return 20000
        else:
            return 5000
    elif office.lower() == "acct":
        if years_in_service >= 10:
            return 15000
        else:
            return 7500
    else:
        return "Invalid office"

# User Input
years = int(input("Enter the number of years in service: "))
office = input("Enter the office (it, acct, hr): ")

# Calculate bonus
bonus = calculate_bonus(years, office)

# Output the result
if isinstance(bonus, int):
    print(f"Bonus for the employee in {office.upper()} with {years} years of service is ${bonus}.")
else:
    print(bonus)
    

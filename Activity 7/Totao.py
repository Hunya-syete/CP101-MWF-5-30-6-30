# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")


# Get input for years in service
try:
    years_in_service = int(input("Enter the number of years in service: "))

    # Get input for office
    print("Select an office from the following: IT, Accounting, HR")
    office = input("Enter office name (IT, Accounting, HR): ").strip().lower()

    # Check if office is valid
    if office not in ["it", "accounting", "hr"]:
        print("Invalid office. Please enter IT, Accounting, or HR.")
    else:
        # Determine the employee's office based on input
        if office == "it":
            office_name = "IT Department"
        elif office == "accounting":
            office_name = "Accounting Department"
        elif office == "hr":
            office_name = "HR Department"

        # Output the results
        print(f"Employee has been in service for {years_in_service} years in the {office_name}.")
except ValueError:
    print("Please enter a valid number for years in service.")

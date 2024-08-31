# Function to calculate gross pay
def calculate_gross_pay(hours, rate_per_hour):
    return hours * rate_per_hour

def main():
    try:
        # Prompt user for the number of hours worked
        hours = float(input("Enter hour: "))
        
        # Prompt user for the rate per hour
        rate_per_hour = float(input("Enter rate: "))
        
        # Calculate the gross pay
        gross_pay = calculate_gross_pay(hours, rate_per_hour)
        
        # Display the gross pay formatted to 2 decimal places
        print(f"Pay {gross_pay:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Entry point of the program
if __name__ == "__main__":
    main()
    # John Renz N. Rosagenia(BSIT 1)

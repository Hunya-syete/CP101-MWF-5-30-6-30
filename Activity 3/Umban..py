# function to calculate gross pay
def calculate_gross_pay(hour, rate_per_hour):
    return hour * rate_per_hour
    
def main():
    try:
        # prompt user for the number of hours worked
        hours = float(input("Enter rate: "))
        
        # prompt user for the rate per hour
        rate_per_hour = float(input("Enter rate: ")) 
        
        # calculate the gross pay
        gross_pay = calculate_gross_pay(hours, rate_per_hour)
        
        # display the gross pay formatted to 2 decimal places
        print(f"pay {gross_pay:.2f}")
        
    except ValueError:
        print("Invalid input, please enter numeric values.")
        
# Entry point of the program
if __name__ == "__main__":
    main()

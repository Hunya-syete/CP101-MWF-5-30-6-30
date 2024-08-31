# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
def compute_gross_pay(hours, rate_per_hour):
    return hours * rate_per_hour

def main():
    try:
        hours = float(input("Enter hours: "))
        rate_per_hour = float(input("Enter rate: "))
        
        if hours < 0 or rate_per_hour < 0:
            print("Hours and rate per hour should be non-negative.")
        else:
            gross_pay = compute_gross_pay(hours, rate_per_hour)
            print(f"Gross pay: ${gross_pay:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

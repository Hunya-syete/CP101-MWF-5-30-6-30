# Record Keeping App

# Dictionary to store records
record_keeping_app = {}

# Display the current records
def display_records():
    if not record_keeping_app:
        print("No records available.")
    else:
        print("Current Records:")
        for key, value in record_keeping_app.items():
            print(f"{key}: {value}")

# Main application loop
while True:
    print("\nPlease choose an option:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")
    
    choice = input("Your choice: ").lower()

    if choice == 'a':
        # Add Data
        key = input("Enter Key: ")
        value = input(f"Enter Value for {key}: ")
        record_keeping_app[key] = value
        print(f"\nData added! {key}: {value}")
        display_records()

    elif choice == 'b':
        # Delete Data
        key = input("Enter Key to delete: ")
        if key in record_keeping_app:
            del record_keeping_app[key]
            print(f"\nData with key '{key}' has been deleted.")
        else:
            print(f"\nKey '{key}' not found.")
        display_records()

    elif choice == 'c':
        # End the application
        print("THANK YOU")
        break

    else:
        print("Invalid choice, please choose again.")

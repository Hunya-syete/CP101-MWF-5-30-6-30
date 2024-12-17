# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
def record_keeping_app():
    records = {}
    
    while True:
        print("\nChoose an option:")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':  # Add Data
            key = input("Enter Key (Lastname): ")
            value = input("Enter Value (Firstname): ")
            records[key] = value
            print(f"Added: {key} -> {value}")
            print("Current Records:", records)
        
        elif choice == '2':  # Delete Data
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]
                print(f"Removed: {key}")
            else:
                print(f"No record found for key: {key}")
            print("Current Records:", records)
        
        elif choice == '3':  # End
            print("THANK YOU!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the application
record_keeping_app()

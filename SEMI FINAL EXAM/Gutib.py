def record_keeping_app():
    records = {}  # Dictionary to store the records

    print("Welcome to the Record Keeping App!")
    
    while True:
        print("\nPlease choose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")
        
        choice = input("Enter your choice (a/b/c): ").strip().lower()
        
        if choice == 'a':  # Add Data
            key = input("Enter Key: ").strip()
            value = input("Enter Value: ").strip()
            records[key] = value  # Add the key-value pair to the dictionary
            print("\nCurrent Records:")
            for k, v in records.items():
                print(f"{k}: {v}")
        
        elif choice == 'b':  # Delete Data
            key_to_delete = input("Enter Key to Delete: ").strip()
            if key_to_delete in records:
                del records[key_to_delete]  # Remove the key-value pair
                print(f"Key '{key_to_delete}' deleted successfully.")
            else:
                print(f"Key '{key_to_delete}' not found.")
            print("\nCurrent Records:")
            for k, v in records.items():
                print(f"{k}: {v}")
        
        elif choice == 'c':  # End
            print("THANK YOU")
            break
        
        else:  # Invalid input
            print("Invalid choice. Please select 'a', 'b', or 'c'.")

# Run the app
record_keeping_app()

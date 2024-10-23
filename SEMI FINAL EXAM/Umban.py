def record_keeping_app():
    records = {}
    
    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")
        choice = input("Enter your choice (a/b/c): ").strip().lower()
        
        if choice == 'a':
            key = input("Enter Key:Lastname ")
            value = input("Enter Value:Firstname ")
            records[key] = value
            print(f"Record added: {key} -> {value}")
            print("Current Records:", records)
        
        elif choice == 'b':
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]
                print(f"Record with key '{key}' has been removed.")
            else:
                print(f"No record found with key '{key}'.")
            print("Current Records:", records)
        
        elif choice == 'c':
            print("THANK YOU")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the app
record_keeping_app()

records = {}

while True:
    print("\nChoose an option:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")
    choice = input("Enter your choice (a/b/c): ").strip().lower()

    if choice == 'a':
        # Add Data
        key = input("Enter Key: ").strip()
        value = input("Enter Value: ").strip()
        records[key] = value
        print(f"\nAdded: {key} -> {value}")
        print("Current Records:", records)

    elif choice == 'b':
        # Delete Data
        key = input("Enter Key: ").strip()
        if key in records:
            del records[key]
            print(f"\nDeleted: {key}")
        else:
            print(f"\nKey '{key}' not found.")
        print("Current Records:", records)

    elif choice == 'c':
        # End
        print("THANK YOU")
        break

    else:
        print("Invalid choice. Please try again.")

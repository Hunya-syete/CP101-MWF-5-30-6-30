def record_keeping_app():
    data_dict = {}

    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")

        choice = input("Enter your choice (a/b/c): ").lower()

        if choice == 'a':
            key = input("Enter Key (e.g., Lastname): ")
            value = input("Enter Value (e.g., Doe): ")
            data_dict[key] = value
            print("\nData Added:")
            print(data_dict)

        elif choice == 'b':
            key = input("Enter the Key to delete: ")
            if key in data_dict:
                del data_dict[key]
                print(f"\nKey '{key}' removed.")
            else:
                print(f"\nKey '{key}' not found.")
            print("Current Data:", data_dict)

        elif choice == 'c':
            print("\nTHANK YOU")
            break

        else:
            print("Invalid choice. Please select a valid option.")

record_keeping_app()

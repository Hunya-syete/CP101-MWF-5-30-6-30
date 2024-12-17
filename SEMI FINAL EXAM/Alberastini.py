selections = str(input("select as option [A,B,C,D]"))

    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")

        choice = input("Enter your choice (a, b, c): ").lower()

        if choice == 'a':
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            data[key] = value
            print(f"Data added. Current data: {data}")

        elif choice == 'b':
            key = input("Enter Key to delete: ")
            if key in data:
                del data[key]
                print(f"Data deleted. Current data: {data}")
            else:
                print(f"Key '{key}' not found.")

        elif choice == 'c':
            print("THANK YOU")
            break

        else:
            print("Invalid option, please choose a, b, or c.")

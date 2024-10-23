records = {}

while True:
    print("\nRecord Keeping App Menu:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

    choice = input("Enter your choice (a-c): ")

    if choice == 'a':
        lastname = input("Enter Lastname: ")
        value = input("Enter Value: ")
        records[lastname] = value
        print("Data added successfully!")
        print("Current Records:", records)
    elif choice == 'b':
        lastname = input("Enter Lastname to delete: ")
        if lastname in records:
            del records[lastname]
            print("Data deleted successfully!")
            print("Current Records:", records)
        else:
            print("Lastname not found.")
    elif choice == 'c':
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Please try again.")
        

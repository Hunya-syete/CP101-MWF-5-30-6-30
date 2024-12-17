#jay taguibolos


record_dict = {}

def record_keeping_app():
    while True:
        print("\nChoose an option:\n a. Add Data\n b. Delete Data\n c. End")
        choice = input("Enter your choice (a/b/c): ").lower()

        if choice == 'a':  
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            record_dict[key] = value
            print(f"\nData Added: {key} : {value}")
            print("Current Records:", record_dict)

        elif choice == 'b':  
            key = input("Enter Key to Delete: ")
            if key in record_dict:
                del record_dict[key]
                print(f"\nData Deleted: {key}")
            else:
                print(f"\nKey '{key}' not found.")
            print("Current Records:", record_dict)

        elif choice == 'c':
            print("\nTHANK YOU")
            break

        else:
            print("\nInvalid choice. Please try again.")


record_keeping_app()

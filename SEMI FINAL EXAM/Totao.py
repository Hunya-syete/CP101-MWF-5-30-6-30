record_dict = {}

def add_data():
    key = input("Enter Key: ")
    if key in record_dict:
        print(f"Key '{key}' already exists. Please choose another key.")
    else:
        value = input("Enter Value: ")
        record_dict[key] = value
        print(f"\nData Added: {key} : {value}")
    print("Current Records:", record_dict)

def delete_data():
    key = input("Enter Key to Delete: ")
    if key in record_dict:
        del record_dict[key]
        print(f"\nData Deleted: {key}")
    else:
        print(f"Key '{key}' not found.")
    print("Current Records:", record_dict)

def show_menu():
    print("\nChoose an option:\n 1. Add Data\n 2. Delete Data\n 3. View All Records\n 4. End")

def record_keeping_app():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_data()
        elif choice == '2':
            delete_data()
        elif choice == '3':
            print("Current Records:", record_dict)
        elif choice == '4':
            print("\nTHANK YOU")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the app
record_keeping_app()

# Record making app 

def show_menu():
    print("\nRecord Management System")
    print("1. Add Data")
    print("2. Delete Data")
    print("3. Dictionary")
    print("4. End Program")

def add_data(records):
    record = input("Enter new record: ")
    records.append(record)
    print(f"Record '{record}' added successfully!")

def delete_data(records):
    if not records:
        print("No records to delete.")
        return

    record = input("Enter the record to delete: ")
    if record in records:
        records.remove(record)
        print(f"Record '{record}' deleted successfully!")
    else:
        print(f"Record '{record}' not found.")

def list_data(records):
    if not records:
        print("No records found.")
    else:
        print("Listing all records:")
        for i, record in enumerate(records, start=1):
            print(f"{i}. {record}")

def main():
    list= []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_data(list)
        elif choice == '2':
            delete_data(list)
        elif choice == '3':
            list_data(list)
        elif choice == '4':
            print("Ending program Thank you...")
            break
        else:
            print("Invalid option, please choose a valid number.")

if __name__ == "__main__":
    main()

class RecordKeeper:
    def __init__(self):
        self.records = {}

    def add_data(self):
        key = input("Enter key: ")
        value = input("Enter value: ")
        self.records[key] = value
        print("Data added successfully!")

    def delete_data(self):
        key = input("Enter key to delete: ")
        if key in self.records:
            del self.records[key]
            print("Data deleted successfully!")
        else:
            print("Key not found!")

    def display_records(self):
        print("\nRecords:")
        for key, value in self.records.items():
            print(f"{key}: {value}")
        print()

def main():
    keeper = RecordKeeper()

    while True:
        print("Record Keeping App")
        print("A. Add Data")
        print("B. Delete Data")
        print("C. End")

        choice = input("Choose an option: ").upper()

        if choice == 'A':
            keeper.add_data()
            keeper.display_records()
        elif choice == 'B':
            keeper.delete_data()
            keeper.display_records()
        elif choice == 'C':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
      

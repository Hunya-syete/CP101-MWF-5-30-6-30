class RecordKeeper:
    def __init__(self):
        self.records = {}

    def add_data(self, key, value):
        self.records[key] = value
        print(f"Added: {key} -> {value}")

    def delete_data(self, key):
        if key in self.records:
            del self.records[key]
            print(f"Deleted: {key}")
        else:
            print(f"Key '{key}' not found.")

    def display_records(self):
        print("\nCurrent Records:")
        for key, value in self.records.items():
            print(f"{key}: {value}")

    def run(self):
        while True:
            print("\nChoose an option:")
            print("a. Add Data")
            print("b. Delete Data")
            print("c. End")
            choice = input("Enter your choice (a/b/c): ").strip().lower()

            if choice == 'a':
                key = input("Enter Key: ").strip()
                value = input("Enter Value: ").strip()
                self.add_data(key, value)
                self.display_records()

            elif choice == 'b':
                key = input("Enter Key: ").strip()
                self.delete_data(key)
                self.display_records()

            elif choice == 'c':
                print("THANK YOU")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = RecordKeeper()
    app.run()

# RECORD KEEPING APP
def add_data(data):
    naming = input("ENTER KEY: ")
    value = input("ENTER VALUE: ")
    data[key] = value
    print(f"ADDED: {key} : {value}")

def data_result(data):
    print("\nDATA RECORDS:")
    for key, value in data.items():
        print(f"{key} : {value}")

def main():
    data = {}

while True:
        print("\n<============== DATA SELECTION =================>")
        print("""
    1. ADD DATA
    2. DELETE DATA
    3. END""")
        samp = input("\nSELECT DATA BY GIVEN: ")
        
        if samp == '1':
            (data)
            data_result(data)
        elif samp == '2':
            key = input("ENTER KEY TO DELETE: ")
            if key in data:
                del data[key]
                print(f"DELETED: {key}")
            else:
                print("KEY NOT FOUND.")
        elif samp == '3':
            print("END OF PROGRAM!")
            break
        else:
            print("DATA CANNOT DEFINE!")

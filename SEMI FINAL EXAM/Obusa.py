user_data = {}

def add_data(key, value):
    new_dict = {key: value}
    user_data.update(new_dict)

def view_data():
    for key, value in user_data.items():
        print(f'Current Key/s: {key}: {value}')

def delete_data(key: str):
    del user_data[key]

while True:
    print('-----{select your options}-----')
    print()
    print('A. Add data \t B. delete data')
    print('C.End program')
    print()
    view_data()
    options: str = input('(A/B/C): ')
    if options.lower() == 'a':
        print('adding data')
        lastname: str = input('lastname: ')
        value = input('value: ')
        add_data(lastname, value)

    if options.lower() == 'b':
        print('deleting data')
        lastname: str = input('lastname: ')
        delete_data(lastname)
        print(user_data)
    if options.lower() == 'c':
        print('THANKYOU')
        break

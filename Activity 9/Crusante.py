Word_Storage = []

print("Word Bank")

while True:
    New = input("Enter: ")
    Word_Storage.append(New)
      
    print("Do You Want to Add More?")
    print("Enter Y(Yes) and N(No)")
  
    Ask = input("'Y' or 'N': ").upper()
    if Ask == 'Y':
        continue 
     
    elif Ask == 'N':
        Number_of_Words = len(Word_Storage)
        print("Words: ", Word_Storage)
        print("Total Number of Words: ", Number_of_Words)
        break




# Anthony Joafil F. Crusante (BSIT 1-B)

words = [ ] 

while True:
    word = input("Enter a word: ")  
    words.append(word)  
    
    again = input("Do you want to enter another word? (Y/N): ").strip().lower()
    if again == 'n':  
        
        break  


print("\nTotal number of words:", len(words))
print("Words entered:")
print(", ".join(words)) 

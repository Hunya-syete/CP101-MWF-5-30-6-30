def word_bank():
    words = [] 
    
    while True:
        word = input("Enter a word: ")
        words.append(word) 

       
        try_again = input("Do you want to enter another word?: ").strip().lower()

        if try_again == 'ry':
            break  

    
    print(f"Total number of words entered: {len(words)}")
    print("Words entered:", ', '.join(words))


word_bank()

def word_bank():
    words = []
    while True:
        word = input("Enter a word: ")
        words.append(word)
        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
        if try_again.lower() != 'y':
            break
    print(f"\nTotal number of words: {len(words)}")
    print("Words entered:", ", ".join(words))

word_bank()

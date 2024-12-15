def word_bank():
    words = []

    while True:
        word = input("Please enter a word: ")
        words.append(word)

        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ").strip().lower()
        if try_again not in ('y', 'yes'):
            break

    print(f"\nTotal number of words: {len(words)}")
    print("Words entered:")
    for w in words:
        print(w)

if __name__ == "__main__":
    word_bank()

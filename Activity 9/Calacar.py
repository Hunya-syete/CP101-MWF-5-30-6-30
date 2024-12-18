res = "y"
wordbank = list()
while res.lower() == "y":
    word = str(input("Enter a word: "))
    wordbank.append(word)
    res = str(input("Would you want to try again? (Y/N)"))
print("============")
print(f"Total Number of Words: {len(wordbank)}")
print("Word in the list:")
for w in wordbank:
    print(w)

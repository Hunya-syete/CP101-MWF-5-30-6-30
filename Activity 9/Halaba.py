words: list = []
i = 0

while True:
    word = input("Add words in your word bank (q to quit): ")
    if word.lower() == 'q':
        print('-=---{words}---=-')
        for word in words:
            if i == 3:
                print(word, end=' ')
                print()
                i = 0
            i += 1
            print(word, end=', ')
        break
    else:
        words.append(word)

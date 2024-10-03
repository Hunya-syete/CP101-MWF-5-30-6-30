def up_low(s):
    upper_case_count = 0
    lower_case_count = 0

    split_s = s.split()

    for word in split_s:

        if word.islower() == False:
            upper_case_count +=1
            lower_case_count += len(word) - 1
        elif word.islower() == True:
            letter_count = len(word)
            lower_case_count += letter_count

    print(f'No. of Upper case characters is {upper_case_count}')
    print(f'No. of Lower case characters is {lower_case_count}')

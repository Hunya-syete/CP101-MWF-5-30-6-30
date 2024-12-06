import random

random_num: int = random.randint(1, 21)
max_attempts: int = 3
attempts: int = 0
is_attempting = True

while is_attempting:
    if attempts == max_attempts:
        print(f'Game Over, reached max attempts of {max_attempts} and the correct num is {random_num}')
        is_attempting = False
        break

    guess = int(input('guess a number: '))
    if guess == random_num:
        print(f'correct! its {random_num}')
        break
    if guess in range(random_num - 5, random_num - 3) or guess in range(random_num + 3, random_num + 5):
        print('hot')
        attempts += 1
    elif guess in range(random_num - 3, random_num - 1) or guess in range(random_num + 1, random_num + 3):
        print('very hot')
        attempts += 1
    elif guess == random_num - 1 or guess == random_num + 1:
        print('SUPERHOT')
        attempts += 1
    else:
        print('far')
        attempts += 1

   

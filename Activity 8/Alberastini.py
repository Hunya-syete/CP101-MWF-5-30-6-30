import random

random_number = random.randint(1, 20)
max_attempts = 3

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 20.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Take a guess: "))

    if guess == random_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < random_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

if guess != random_number:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {random_number}.")

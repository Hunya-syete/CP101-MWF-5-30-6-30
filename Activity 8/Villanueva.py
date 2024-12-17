import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    max_attempts = 3
    attempts = 0

    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20.")
                continue

            if guess == number_to_guess:
                print("Congratulations! You guessed the number correctly.")
                break
            elif guess < number_to_guess:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

            if attempts == max_attempts:
                print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()p

import random
def guess_the_number():
   
    secret_number = random.randint(1, 30)
    max_attempts = 5
    
    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 30.")
    print(f"You have {max_attempts} attempts to guess it correctly.")

     for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Take a guess: "))
            
            if guess < 1 or guess > 30:
                print("Please enter a number between 1 and 30.")
                continue
            
            if guess == secret_number:
                print("Congratulations! You guessed the number correctly!")
                break
            elif guess < secret_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

guess_the_number()

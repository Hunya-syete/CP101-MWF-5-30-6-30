import random

def guess_the_number():
    target_number = random.randint(1, 20)
    
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 20. You have 3 attempts.")

    for attempt in range(3):
        guess = int(input(f"Attempt {attempt + 1}: Your guess: "))
        
        if guess == target_number:
            print(f"Correct! The number was {target_number}. You win!")
            return
        elif guess < target_number:
            print("Too low! guess again.")
        else:
            print("Too high! guess again.")

    print(f"Out of attempts! The number was {target_number}. Better luck next time.")

guess_the_number()

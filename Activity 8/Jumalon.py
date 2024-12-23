import random

def play_game():
    lowest_num = 1
    highest_num = 20
    answer = random.randint(lowest_num, highest_num)
    guesses = 0

    print("WELCOME TO GUESSING NUMBER!")
    print(f"Select a number between {lowest_num} - {highest_num}:")
    print("\n")
    while True:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print("WARNING: OUT OF RANGE!")
                print(f"Select a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too Low! Try Again!")
            elif guess > answer:
                print("Too High! Try Again!")
            else:
                print(f"CORRECT! The Answer was {answer}")
                print(f"Number Of Guesses: {guesses}")
                break
        else:
            print("INVALID GUESS!")
            print(f"Select a number between {lowest_num} and {highest_num}")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break
        

if __name__ == "__main__":
    main()

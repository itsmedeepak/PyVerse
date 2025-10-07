import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess (1–100): "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please guess within the range 1–100.")
                continue
            if guess < secret_number:
                print("Too low! Try a higher number")
            elif guess > secret_number:
                print("Too high! Try a lower number")
            else:
                print(f" Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == 'y':
        guess_the_number()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    guess_the_number()

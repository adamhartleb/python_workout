import random

def guessing_game():
    guess_count = 3
    number = random.randint(0, 100)

    print("Welcome to the guessing game. You have 3 guesses to guess the number I'm thinking of.")

    while guess_count > 0:
        guess = int(input("Pick a number between 0 and 100: "))

        if number > guess:
            print("The number is higher than your guess.")
            guess_count -= 1
        elif number < guess:
            print("The number is lower than your guess.")
            guess_count -= 1
        else:
            print("Congratulations, you got it right!")
            break
        print(f"You have {guess_count} guess(es) remaining.")

guessing_game()
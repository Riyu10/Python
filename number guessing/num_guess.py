import random

def number_guessing_game():
    # Introduction and mode selection
    print("Welcome to the Number Guessing Game!")
    print("Choose your mode:")
    print("1. Easy ")
    print("2. Hard ")
    
    # Get the player's choice for the game mode
    while True:
        mode = input("Enter 1 for Easy or 2 for Hard: ")
        if mode == '1':
            max_attempts = 10
            break
        elif mode == '2':
            max_attempts = 5
            break
        else:
            print("Invalid choice. Please enter 1 for Easy or 2 for Hard.")
    
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print(f"You have chosen the {'Easy' if max_attempts == 10 else 'Hard'} mode. You have {max_attempts} attempts to guess the number.")

    # Game loop
    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        # Validate if the input is a number
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts!")
            break
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
number_guessing_game()
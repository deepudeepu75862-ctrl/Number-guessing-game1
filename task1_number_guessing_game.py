import random

def play_game():
    """Play a simple number guessing game."""
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        user_input = input("Enter your guess (or q to quit): ").strip()

        if user_input.lower() == "q":
            print(f"The number was {secret_number}. Thanks for playing!")
            break

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a whole number between 1 and 10.")
            continue

        if not 1 <= guess <= 10:
            print("Your guess must be between 1 and 10.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempt(s).")
            break

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

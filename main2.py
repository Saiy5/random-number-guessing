import random

# Define the file name to store winner details
WINNER_FILE = "winner.txt"

def save_winner(name, attempts, correct_number):
    """Save the winner's name, attempts, and correct number to the file, overwriting the previous winner."""
    with open(WINNER_FILE, "w") as f:
        f.write(f"Winner: {name}\n")
        f.write(f"Correct Number: {correct_number}\n")
        f.write(f"Attempts: {attempts}\n")

def play_game():
    print("Welcome to the Number Guessing Game!")
    
    # Ask for the player's name
    name = input("Enter your name: ").strip()

    # Generate a random number
    correct_number = random.randint(1, 100)
    guesses = 0  # Counter for attempts

    while True:
        try:
            # User input
            a = int(input("Guess the number between 1 and 100: "))
            guesses += 1  # Increment attempt count

            # Save every guess to the file
            with open(WINNER_FILE, "a") as f:
                f.write(f"Attempt {guesses}: {a}\n")

            if a > correct_number:
                print("Lower number, please.")
            elif a < correct_number:
                print("Higher number, please.")
            else:
                print(f"🎉 Congratulations {name}! You guessed the number {correct_number} correctly in {guesses} attempts.")

                # Overwrite the file with new winner details
                save_winner(name, guesses, correct_number)
                break  # Exit the loop when guessed correctly
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_game()

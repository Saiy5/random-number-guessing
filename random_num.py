from random import randint
# from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual number
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You have got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Choosing a number between 1 to 100
def game():
    # print(logo)
    print("Welcome to a number guessing game!")
    print("I'm thinking about a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"The currect answer is: {answer}")

    turns = set_difficulty()

    # Repete the gussing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemptes remening to guess the number")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")

# Track the number of turns and reduce by 1 if they get it wrong

if __name__ == "__main__":
    game()
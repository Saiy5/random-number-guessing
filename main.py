import random

def guess_the_number():
    print("Welcome to the number Guessing game!")
    n = random.randint(1, 100)  #Generate a random number between 1 to 100
    guesses = 0

    while True: #This conditon should always be true
        try:
            a = int(input("Guess the number between 1 to 100: "))
            guesses +=1  #Incorrect number count

            if(a>n):
                print("Lower Number Please")
                
            elif(a<n):
                print("Higher Number please")

            else:
                print(f"You have guessed the number {n} correctly in {guesses} attempts")
                break #Exit the loop when you guess the number

        except ValueError as v:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
                
        
if __name__ == "__main__":
    guess_the_number()

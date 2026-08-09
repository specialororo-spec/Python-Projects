import random

print("Welcome to my Number Guessing Game!")
while True:
    number = random.randint(1, 100)
    attempts = 0
    print("Guess a number from 1 to 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Error, Number either too high or low")
                continue
            attempts += 1
            if guess > number:
                print("Too High")
            elif guess < number:
                print("Too Low")
            else:
                print("You are correct")
                print(f"Number of attempts: {attempts}")
                break

        except ValueError:
            print("Wrong input! Please enter a whole number.")
    play_again = input("Do you want to play again? (Yes/No?): ")
    if play_again != 'Yes':
        break

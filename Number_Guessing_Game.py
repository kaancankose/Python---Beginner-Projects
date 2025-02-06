import random

random_number = random.randint(1, 100)
guess_attempts = 5

print("Guess a number between 1 and 100!")

while guess_attempts > 0:
    guess = int(input("Your guess: "))

    if guess == random_number:
        print("Congratulations! You guessed it right 🎉")
        break
    elif guess < random_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

    guess_attempts -= 1
    print(f"Remaining attempts: {guess_attempts}")

if guess_attempts == 0:
    print(f"Sorry, you lost. The correct number was: {random_number}")

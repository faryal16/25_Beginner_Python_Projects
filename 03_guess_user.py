import random


print("\n🎉 Welcome to the Number Guessing Game! 🎉\n")

# generate a random number between 1 to 50
secret_number = random.randint(1,50)

# Ask the playes
attempts = 0
while True:
    guess= int(input("\nEnter Your Number: "))
    attempts += 1

    if guess < secret_number:
        print("\nToo Low! Try Again")

    elif guess > secret_number:
        print("\nToo High! Try Again\n")
    else:
         print(f" \nYes {secret_number} was correct!\n🎉 Congratulations! You guessed it in {attempts} attempts.")
         break
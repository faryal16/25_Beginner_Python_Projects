import random


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    """Sets the number of attempts based on difficulty level."""
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
    
def check_answer(guessed_number, answer, attempts):
    """Checks the guessed number against the answer and returns remaining attempts."""
    if guessed_number < answer:
        print("Your guess is too low.")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"\n🎉 Woooo! You got it! Yes, the answer was {answer}! 🎉")
        return None  # Returning None to indicate a correct guess

def game():
    """Main function to run the game."""
    print("Hey there! Welcome to my game zone 🎮")
    print("""
🐬  🎀  𝒢𝒰𝐸𝒮𝒮 𝒯𝐻𝐸 𝒩𝒰𝑀𝐵𝐸𝑅  🎀  🐬""")
    print("\nLet me think of a number between 1 to 50...\n")

    answer = random.randint(1, 50)
    # print(answer)  # Debugging (uncomment if needed)

    level = input("\n🎉So, how daring do you feel today? Choose 'easy' or 'hard': ").lower()

    attempts = set_difficulty(level)
    guessed_number = 0

    while guessed_number != answer and attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the right number.")

        try:
            guessed_number = int(input("Guess a number: "))
        except ValueError:
            print("🚨 Invalid input! Please enter a number.")
            continue  # Skip the rest of the loop and retry

        attempts = check_answer(guessed_number, answer, attempts)

        if attempts is None:  # Correct answer
            break
        elif attempts == 0:
            print("\n💔 Oh no! You're out of guesses. You lose! The correct answer was:", answer)
            return
        else:
            print("🔄 Try again!")

game()

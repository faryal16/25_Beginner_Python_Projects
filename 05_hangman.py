import random

# Hangman stages (ASCII art)
hangman_stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    =========
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    =========
    """
]

# Word list for the game
word_list = ["python", "developer", "computer", "programming", "hangman", "javascript", "nextjs", "sanity"]

# Randomly select a word
word = random.choice(word_list)
word_length = len(word)

# Create display (hidden word)
display = ["_"] * word_length

# Set the number of attempts
attempts = 6
guessed_letters = []

print("\n🎉 Welcome to Hangman! 🎉")
print("Try to guess the word letter by letter.")
print("You have 6 attempts to guess correctly.\n")

# Main game loop
while "_" in display and attempts > 0:
    print(hangman_stages[attempts])  # Show hangman stage
    print(" ".join(display))  # Show the current progress
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Please enter a single letter.")
        continue

    # If letter is already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)  # Add to guessed list

    # Check if guess is in the word
    if guess in word:
        print(f"✅ Good job! '{guess}' is in the word!")
        for i in range(word_length):
            if word[i] == guess:
                display[i] = guess  # Reveal the letter
    else:
        attempts -= 1
        print(f"❌ Wrong guess! '{guess}' is NOT in the word. {attempts} attempts left.")

# Game Over - Check Win/Loss
if "_" not in display:
    print(f"\n🎉 Congratulations! You guessed the word: {word.upper()} 🎊")
else:
    print(hangman_stages[0])  # Show final hangman
    print(f"\n😢 You ran out of attempts! The word was: {word.upper()}")

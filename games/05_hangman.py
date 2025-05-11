import streamlit as st
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

# Streamlit interface to play Hangman
def run():
    st.title("🎉 Welcome to Hangman! 🎉")
    st.markdown("Try to guess the word letter by letter. You have 6 attempts to guess correctly.")

    # Initialize game state in session_state
    if "word" not in st.session_state:
        st.session_state.word = random.choice(word_list)  # Randomly select a word
        st.session_state.word_length = len(st.session_state.word)
        st.session_state.display = ["_"] * st.session_state.word_length  # Display (hidden word)
        st.session_state.attempts = 6
        st.session_state.guessed_letters = []

    # Show current game progress
    st.write("### Word: " + " ".join(st.session_state.display))  # Show the current progress
    st.markdown(f"### Hangman Stage: \n{hangman_stages[st.session_state.attempts]}")  # Show hangman stage

    # Input for guess
    guess = st.text_input("Guess a letter:", max_chars=1).lower()

    # Handle guess submission
    if guess:
        if len(guess) != 1 or not guess.isalpha():
            st.warning("❌ Invalid input! Please enter a single letter.")
        elif guess in st.session_state.guessed_letters:
            st.warning("⚠️ You already guessed that letter!")
        else:
            st.session_state.guessed_letters.append(guess)  # Add to guessed list

            # Check if guess is in the word
            if guess in st.session_state.word:
                st.success(f"✅ Good job! '{guess}' is in the word!")
                for i in range(st.session_state.word_length):
                    if st.session_state.word[i] == guess:
                        st.session_state.display[i] = guess  # Reveal the letter
            else:
                st.error(f"❌ Wrong guess! '{guess}' is NOT in the word.")
                st.session_state.attempts -= 1

    # Check for game over or win
    if "_" not in st.session_state.display:
        st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word.upper()} 🎊")
        if st.button("🔄 Play Again"):
            reset_game()

    elif st.session_state.attempts == 0:
        st.error(f"😢 You ran out of attempts! The word was: {st.session_state.word.upper()}")
        if st.button("🔄 Play Again"):
            reset_game()

def reset_game():
    """Reset the game state"""
    for key in ["word", "word_length", "display", "attempts", "guessed_letters"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

if __name__ == "__main__":
    run()

import streamlit as st
import random

def run():
    st.title("🎉 Welcome to the Number Guessing Game! 🎉")

    # Generate a random number between 1 and 50 if it's not already generated
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 50)
        st.session_state.attempts = 0

    # Display attempts remaining
    st.markdown(f"### Attempts: {st.session_state.attempts}")

    # Input for user's guess
    guess = st.number_input("Enter Your Guess (1-50):", min_value=1, max_value=50, step=1)

    # Button to submit guess
    if st.button("Submit Guess"):
        st.session_state.attempts += 1  # Increment attempts
        
        if guess < st.session_state.secret_number:
            st.warning("Too Low! Try Again")
        elif guess > st.session_state.secret_number:
            st.warning("Too High! Try Again")
        else:
            st.success(f"Yes! {st.session_state.secret_number} was correct! 🎉")
            st.success(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.secret_number = random.randint(1, 50)  # Reset secret number for next round
            st.session_state.attempts = 0  # Reset attempts for next round

    # Button to reset the game
    if st.button("🔄 Play Again"):
        st.session_state.secret_number = random.randint(1, 50)  # Reset secret number
        st.session_state.attempts = 0  # Reset attempts
        st.rerun()  # Restart the app to simulate a new game

if __name__ == "__main__":
    run()

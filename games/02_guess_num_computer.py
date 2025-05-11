import streamlit as st
import random

def run():
    st.title("🔢 Guess the Number")
    st.markdown("I'm thinking of a number between **1 and 50**. Can you guess it?")


    # --- Initialize game state ---
    if "answer" not in st.session_state:
        st.session_state.answer = random.randint(1, 50)
        st.session_state.attempts = 0
        st.session_state.max_attempts = 0
        st.session_state.game_active = False

    # --- Choose difficulty ---
    if not st.session_state.game_active:
        st.markdown("### Choose Difficulty")
        col1, col2 = st.columns(2)
        if col1.button("Easy 😌 (10 attempts)"):
            st.session_state.max_attempts = 10
            st.session_state.attempts = 0
            st.session_state.game_active = True
        if col2.button("Hard 😈 (5 attempts)"):
            st.session_state.max_attempts = 5
            st.session_state.attempts = 0
            st.session_state.game_active = True

    # --- Main game ---
    if st.session_state.game_active:
        st.markdown(f"### Attempts remaining: {st.session_state.max_attempts - st.session_state.attempts}")
        guess = st.number_input("Enter your guess (1-50):", min_value=1, max_value=50, step=1)

        if st.button("Submit Guess"):
            st.session_state.attempts += 1

            if guess < st.session_state.answer:
                st.warning("Too low! Try again.")
            elif guess > st.session_state.answer:
                st.warning("Too high! Try again.")
            else:
                st.success(f"🎉 You got it! The answer was {st.session_state.answer}.")
                st.session_state.game_active = False

            if st.session_state.attempts >= st.session_state.max_attempts and st.session_state.game_active:
                st.error(f"💔 Out of attempts! The number was {st.session_state.answer}.")
                st.session_state.game_active = False

    # --- Play Again & Reset buttons in columns ---
    if not st.session_state.game_active:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎮 Play Again"):
                for key in ["answer", "attempts", "max_attempts", "game_active"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()

        with col2:
            if st.button("🔄 Reset Game"):
                for key in ["answer", "attempts", "max_attempts", "game_active"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()


if __name__ == "__main__":
    run()

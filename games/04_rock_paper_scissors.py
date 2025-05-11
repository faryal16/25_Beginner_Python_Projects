# Rules of this game
# Rock Paper Scissors
# Rock "Rocks wins against Scissors"
# Paper "Paper wins against Rocks"
# Scissors "Scissors wins againt paper"
import streamlit as st
import random

def run():
    st.title("Rock-Paper-Scissors! ✊✋✌️")
    st.markdown("Welcome to the Rock-Paper-Scissors game! Choose your move and see if you win! 🎮")

    # Choices for the game
    choices = ["Rock ✊", "Paper ✋", "Scissors ✌️"]

    # Display the buttons for the user's choice
    st.markdown("### Choose your move:")
    user_choice = None
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Rock ✊"):
            user_choice = 0
    with col2:
        if st.button("Paper ✋"):
            user_choice = 1
    with col3:
        if st.button("Scissors ✌️"):
            user_choice = 2

    if user_choice is not None:
        # Generate computer's choice
        computer_choice = random.randint(0, 2)

        # Display choices
        st.write(f"\n**You chose:** {choices[user_choice]}")
        st.write(f"**Computer chose:** {choices[computer_choice]}\n")

        # Determine the winner
        if user_choice == computer_choice:
            st.write("🤝 It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            st.write("✅ **You win!** 🎉")
        else:
            st.write("❌ **You lose!** 😢")

        # Reset game button
        if st.button("🔄 Play Again"):
            st.rerun()

if __name__ == "__main__":
    run()

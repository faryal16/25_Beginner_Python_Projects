import streamlit as st
import time
import random
from tqdm import tqdm

# Function to handle countdown timer
def countdown_timer(seconds):
    st.write("\n🚀 Countdown Timer Started! 🚀\n")
    
    for remaining in tqdm(range(seconds, 0, -1), desc="⏳ Time Left", ncols=75):
        time.sleep(1)  # Delay for 1 second per step
    
    st.write("\n🎉 Time's up! 🎉")
    fun_messages = [
        "Boom! 💥 Time just vanished!",
        "Tick-tock, tick-tock...⏰ And it's over!",
        "Mission Complete! ✅",
        "You made it! Now go have fun! 🎈",
    ]
    
    st.write(random.choice(fun_messages))

# Main run function for Streamlit
def run():
    st.title("⏲️ Countdown Timer")

    # Take input from user using Streamlit
    countdown_time = st.slider("Set countdown time (seconds):", min_value=1, max_value=600, value=30)

    # Start countdown timer when button is clicked
    if st.button("Start Countdown"):
        countdown_timer(countdown_time)

# Run the Streamlit app
if __name__ == "__main__":
    run()

import time
import random
from tqdm import tqdm

def countdown_timer(seconds):
    print("\n🚀 Countdown Timer Started! 🚀\n")
    
    for remaining in tqdm(range(seconds, 0, -1), desc="⏳ Time Left", ncols=75):
        time.sleep(1)  # Delay for 1 second per step
    
    print("\n🎉 Time's up! 🎉")
    fun_messages = [
        "Boom! 💥 Time just vanished!",
        "Tick-tock, tick-tock...⏰ And it's over!",
        "Mission Complete! ✅",
        "You made it! Now go have fun! 🎈",
    ]
    
    print(random.choice(fun_messages))

# Set the countdown time (change as needed)
countdown_time = int(input("⏲️ Enter countdown time in seconds: "))
countdown_timer(countdown_time)

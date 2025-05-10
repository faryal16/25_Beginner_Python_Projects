# Rules of this game
# Rock Paper Scissors
# Rock "Rocks wins against Scissors"
# Paper "Paper wins against Rocks"
# Scissors "Scissors wins againt paper"

import random

print("\nWelcome to Rock-Paper-Scissors! ✊✋✌️")

choices = ["Rock ✊", "Paper ✋", "Scissors ✌️"]

while True:  # Keep asking until a valid input is received
    try:
        user_choice = int(input("\nEnter your choice:\n0 for Rock ✊, 1 for Paper ✋, 2 for Scissors ✌️\nYour choice: "))

        if user_choice not in [0, 1, 2]:
            print("❌ Invalid choice! Please enter 0, 1, or 2.")
            continue  # Ask again if input is invalid
        
        break  # Exit loop when valid input is given

    except ValueError:
        print("❌ Invalid input! Please enter a number (0, 1, or 2).")

# Computer's choice
computer_choice = random.randint(0, 2)

print(f"\nYou chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}\n")

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw! 🤝")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("✅ You win! 🎉")
else:
    print("❌ You lose! 😢")

from random import randint

print("Welcome to the Madlib Game!")
playing = input("Let's play, shall we? (Yes/No): ").strip()

if playing.lower() not in ["yes", "y"]:
    print("Okay, maybe next time!")
    quit()

print("\nOkay, let's play the game!\n")

# Getting user input
noun1 = input("Enter your Name: ")
noun2 = input("Enter your Friend's Name: ")
noun3 = input("Enter another Friend's Name: ")
place = input("Enter a place name: ")
adjective1 = input("Enter an Adjective: ")
adjective2 = input("Enter another Adjective: ")
adjective3 = input("Enter one more Adjective: ")
adverb1 = input("Enter an Adverb: ")
adverb2 = input("Enter another Adverb: ")
exclamation = input("Enter an Emotion: ")

# Print story using f-strings
story = f"""
One day, {noun1} and their two best friends, {noun2} and {noun3}, decided to go on an adventure to {place}. It was a {adjective1} day, with the sun shining brightly in the sky.

As they arrived, they noticed something {adjective2} in the distance. Curious, they walked {adverb1} towards it, only to realize it was a hidden treasure chest! "{exclamation}!" they all shouted in excitement.

Just as they were about to open it, a {adjective3} gust of wind blew, and suddenly, the ground started shaking {adverb2}. Was it a trap? Or was it magic? They looked at each other, unsure of what to do next.
"""

print(story)

import streamlit as st

def run():
    # st.set_page_config(page_title="Madlib Game", page_icon="📖")

    st.title("📖 Madlib Adventure Game")
    st.markdown("Fill in the blanks below to create your own silly story!")

    # Form for inputs
    with st.form("madlib_form"):
        noun1 = st.text_input("Enter your Name:")
        noun2 = st.text_input("Enter your Friend's Name:")
        noun3 = st.text_input("Enter another Friend's Name:")
        place = st.text_input("Enter a place name:")
        adjective1 = st.text_input("Enter an Adjective:")
        adjective2 = st.text_input("Enter another Adjective:")
        adjective3 = st.text_input("Enter one more Adjective:")
        adverb1 = st.text_input("Enter an Adverb:")
        adverb2 = st.text_input("Enter another Adverb:")
        exclamation = st.text_input("Enter an Emotion:")

        submitted = st.form_submit_button("🎉 Tell My Story")

    # Display the story
    if submitted:
        if all([noun1, noun2, noun3, place, adjective1, adjective2, adjective3, adverb1, adverb2, exclamation]):
            st.success("Here's your custom Madlib story:")

            story = f"""
            One day, **{noun1}** and their two best friends, **{noun2}** and **{noun3}**, decided to go on an adventure to **{place}**.
            It was a **{adjective1}** day, with the sun shining brightly in the sky.

            As they arrived, they noticed something **{adjective2}** in the distance.
            Curious, they walked **{adverb1}** towards it, only to realize it was a hidden treasure chest!

            "**{exclamation}!**" they all shouted in excitement.

            Just as they were about to open it, a **{adjective3}** gust of wind blew,
            and suddenly, the ground started shaking **{adverb2}**.

            Was it a trap? Or was it magic?
            They looked at each other, unsure of what to do next...
            """

            st.markdown(story)
        else:
            st.error("Please fill out all fields to create the story!")

if __name__ == "__main__":
    run()
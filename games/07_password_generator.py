import streamlit as st
import random
import string

# Function to generate a secure password
def generate_password(password_len):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Create character pool
    s = list(s1 + s2 + s3 + s4)
    random.shuffle(s)

    # Generate password
    password = "".join(s[:password_len])
    return password

# Main run function for Streamlit
def run():
    st.title("🔐 Secure Password Generator")

    # Asking user for password length
    password_len = st.slider("Select Password Length:", 6, 12, 8)

    # Generate password when button is clicked
    if st.button("Generate Password"):
        if 6 <= password_len <= 12:
            password = generate_password(password_len)
            st.success(f"✅ Your Secure Password: {password}")
        else:
            st.error("⚠️ Password length must be between 6 and 12 characters.")

# Run the Streamlit app
if __name__ == "__main__":
    run()

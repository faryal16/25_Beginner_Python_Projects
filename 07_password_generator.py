import random
import string

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Asking user for password length
    while True:
        try:
            passwordLen = int(input("\n🔐 Enter desired password length : "))
            if 6 <= passwordLen <= 12:
                break
            else:
                print("\n⚠️ Password length must be between 6 and 12!")
        except ValueError:
            print("\n❌ Invalid input! Please enter a number between 6 and 12.")

    # Create character pool
    s = list(s1 + s2 + s3 + s4)
    random.shuffle(s)

    # Generate password
    password = "".join(s[:passwordLen])
    print(f"\n✅ Your Secure Password: {password}")

import random
import string

def generate_password(length=12):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    
    all_chars = letters + digits + special_chars
  
    if length < 8:
        length = 8

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        password = generate_password(password_length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid password length (an integer).")
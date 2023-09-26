import random
import string

def generate_random_password(length=12):
    # Define the characters to be used in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    # Make sure each type of character is present at least once
    password_chars = random.choices(uppercase_letters, k=1) + random.choices(lowercase_letters, k=1) + random.choices(digits, k=2) + random.choices(punctuation, k=1)

    # Generate the rest of the password by randomly selecting characters from the defined pool
    remaining_length = length - 5  # 5 = 1 uppercase + 1 lowercase + 2 digits + 1 punctuation
    password_chars += random.choices(uppercase_letters + lowercase_letters + digits + punctuation, k=remaining_length)

    # Shuffle the characters to mix up the order
    random.shuffle(password_chars)

    # Combine the characters into the final password
    password = ''.join(password_chars)

    return password

# Example usage:
random_password = generate_random_password()
print(random_password)







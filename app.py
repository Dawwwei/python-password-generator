import random
import string

def generate_password(length, uppercase, lowercase, numbers, symbols):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one option")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please, enter a valid length of password")
        return

    uppercase = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (Y/N): ").lower() == 'y'
    numbers = input("Include numbers? (Y/N): ").lower() == 'y'
    symbols = input("Include symbols? (Y/N): ").lower() == 'y'

    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    if password:
        print("Generated password: ", password)
    else:
        print("There was an error while generating your password")

if __name__ == "__main__":
    main()
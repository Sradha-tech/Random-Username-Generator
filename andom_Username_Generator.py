# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Funky", "Witty", "Epic", "Swift", "Sneaky", "Chill", "Mighty"]
nouns = ["Tiger", "Dragon", "Ninja", "Panda", "Phoenix", "Gamer", "Wizard", "Samurai", "Shadow", "Knight"]

# Function to generate a random username
def generate_username(add_numbers=True, add_special_chars=False, length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if add_numbers:
        username += str(random.randint(10, 99))  # Add a random number

    if add_special_chars:
        username += random.choice("!@#$%^&*")

    if length and len(username) > length:
        username = username[:length]  # Trim username to the desired length

    return username

# Function to save usernames to a file
def save_to_file(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"✅ Saved {len(usernames)} usernames to {filename}")

# Interactive user input
def main():
    print("✨ Welcome to the Random Username Generator ✨")
    
    add_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    add_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    length = input("Set a max username length (or press Enter to skip): ").strip()
    length = int(length) if length.isdigit() else None
    num_usernames = int(input("How many usernames do you want to generate?: "))

    usernames = [generate_username(add_numbers, add_special_chars, length) for _ in range(num_usernames)]
    
    print("\nGenerated Usernames: ")
    for username in usernames:
        print("👉", username)

    save_choice = input("\nSave usernames to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_to_file(usernames)

if __name__ == "__main__":
    main()

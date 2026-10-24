import string
import random

def generate_password():
    print("--- Random Password Generator ---")
    
    # 1. Prompt user for password length (minimum 8 characters enforced)
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("Error: Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for length.")

    # 2. Prompt user for character types selection
    print("\nSelect character types to include:")
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters (a-z)? (y/n): ").strip().lower() == 'y'
    use_nums = input("Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
    use_syms = input("Include symbols (!@#$%^&*...)? (y/n): ").strip().lower() == 'y'

    # Validation: at least 2 character types must be selected
    selected_types = sum([use_upper, use_lower, use_nums, use_syms])
    if selected_types < 2:
        print("\nError: You must select at least 2 character types! Please try again.\n")
        return generate_password()

    # Build character pool and ensure at least one of each selected type is included
    char_pool = ""
    mandatory_chars = []

    if use_upper:
        char_pool += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        mandatory_chars.append(random.choice(string.ascii_lowercase))
    if use_nums:
        char_pool += string.digits
        mandatory_chars.append(random.choice(string.digits))
    if use_syms:
        char_pool += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))

    # Generate remaining characters
    remaining_length = length - len(mandatory_chars)
    password_chars = mandatory_chars + [random.choice(char_pool) for _ in range(remaining_length)]
    
    # Shuffle list for randomness
    random.shuffle(password_chars)
    final_password = "".join(password_chars)

    print(f"\nGenerated Secure Password: {final_password}")
    
    # Option to generate another password without restarting
    choice = input("\nWould you like to generate another password? (y/n): ").strip().lower()
    if choice == 'y':
        print("\n" + "="*40 + "\n")
        generate_password()
    else:
        print("Thank you for using Random Password Generator!")

if __name__ == "__main__":
    generate_password()

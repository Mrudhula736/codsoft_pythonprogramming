import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters + string.digits
    
    if complexity == "medium":
        characters += string.punctuation
    elif complexity == "high":
        characters += string.ascii_uppercase + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity (low, medium, high): ").lower()

    if complexity not in ["low", "medium", "high"]:
        print("Invalid complexity level.")
        return

    password = generate_password(length, complexity)

    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()


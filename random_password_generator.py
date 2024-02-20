import random
import string

def generate_password(length=8, complexity='medium'):
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ").lower()
    while complexity not in ['low', 'medium', 'high']:
        print("Invalid complexity level. Please enter 'low', 'medium', or 'high'.")
        complexity = input("Enter the complexity level (low/medium/high): ").lower()

    password = generate_password(length, complexity)
    print("Generated Password:", password)

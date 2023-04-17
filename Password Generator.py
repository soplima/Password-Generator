import random
import string

def generate_password(length, complexity):
    # Define the set of characters that can be used in the password
    if complexity == 'weak':
        charset = string.ascii_lowercase
    elif complexity == 'strong':
        charset = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError('Invalid complexity level')
    
    # Generate the password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

# Get user input for password length and complexity
length = int(input('Enter password length: '))
complexity = input('Enter password complexity (weak/strong): ')

# Generate and print the password
password = generate_password(length, complexity)
print(f'Your password is: {password}')

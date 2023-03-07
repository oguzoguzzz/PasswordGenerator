import random
import string

def generate_password(length,complexity):
    """ Generate a random password."""
    
    # Define character sets for each complexity level

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Create a list of characters to use based on specified complexity

    if complexity == "low":
        char_set = lower + upper
    
    elif complexity == "medium":
        char_set = lower + upper + digits
    else:    
        char_set = lower + upper + digits + symbols

    # Generate a random password using the selected character set
    password = ''.join(random.choice(char_set) for i in range(length))
    return password

# Example usage
password = generate_password(8,"")
print(password)

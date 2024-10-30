# import string

# def check_pangram(text):
#     alphabet = set(string.ascii_lowercase)
#     return all(letter in text.lower() for letter in alphabet)

# user_input = input("Enter a string: ")
# if check_pangram(user_input):
#     print("The string contains all letters of the alphabet.")
# else:
#     print("The string does not contain all letters of the alphabet.")

import string

def is_pangram(s):
    # Convert the string to lowercase and remove non-alphabetic characters
    s = s.lower()
    
    # Create a set of all unique alphabetic characters in the string
    letters_in_string = set([char for char in s if char.isalpha()])
    
    # Compare with the set of all letters in the alphabet
    return len(letters_in_string) == 26

# Example usage:
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output will be True
print(is_pangram("Hello, World!"))  # Output will be False

import string

def is_pangram(s):
    # Create a set of all lowercase letters in the alphabet
    alphabet = set(string.ascii_lowercase)
    
    # Convert the string to lowercase and create a set of the letters in the string
    return alphabet <= set(s.lower())

# Example usage:
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output will be True
print(is_pangram("Hello, World!"))  # Output will be False
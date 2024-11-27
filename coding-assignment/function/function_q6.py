# Write a function to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

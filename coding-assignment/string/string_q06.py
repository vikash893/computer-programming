# Check if a string is a palindrome by ignoring spaces and non-alphanumeric characters.
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example:
text = "A man, a plan, a canal: Panama"
print(is_palindrome(text))  # Output: True

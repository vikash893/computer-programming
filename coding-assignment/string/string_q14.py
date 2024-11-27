# Write a function to find the first non-repeating character in a string.
def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# Test the function
print(first_non_repeating_char("swiss"))  # Output: w

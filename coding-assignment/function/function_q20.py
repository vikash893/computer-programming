# Write a function to find the longest word in a string

def longest_word(s):
    words = s.split()
    return max(words, key=len)

# Test the function
print(longest_word("The quick brown fox jumped over the lazy dog"))  # Output: jumped

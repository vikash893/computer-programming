# Write a function to check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Test the function
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))  # Output: False

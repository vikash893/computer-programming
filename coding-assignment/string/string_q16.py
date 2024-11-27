# Write a function to count the number of vowels in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test the function
print(count_vowels("hello world"))  # Output: 3

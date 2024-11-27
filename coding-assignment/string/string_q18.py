# Write a function to replace all vowels in a string with a specified character.
def replace_vowels(s, replacement):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += replacement
        else:
            result += char
    return result

# Test the function
print(replace_vowels("hello world", "*"))  # Output: h*ll* w*rld

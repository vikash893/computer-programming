# Write a function to remove duplicate characters from a string.
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

# Test the function
print(remove_duplicates("programming"))  # Output: progamin

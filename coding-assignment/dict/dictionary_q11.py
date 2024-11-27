# Write a function to check if a key exists in a dictionary.

def key_exists(d, key):
    return key in d

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(key_exists(my_dict, "b"))  # Output: True
print(key_exists(my_dict, "d"))  # Output: False

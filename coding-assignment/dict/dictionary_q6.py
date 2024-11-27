# Write a function to remove a key from a dictionary.

def remove_key(d, key):
    if key in d:
        del d[key]
    return d

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(remove_key(my_dict, "b"))  # Output: {'a': 1, 'c': 3}

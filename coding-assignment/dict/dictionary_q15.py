# Write a function to convert two lists into a dictionary

def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Test the function
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(lists_to_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}

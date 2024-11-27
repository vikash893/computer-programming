# Write a function to sort a dictionary by key.

def sort_by_key(d):
    return dict(sorted(d.items()))

# Test the function
my_dict = {"b": 2, "a": 1, "c": 3}
print(sort_by_key(my_dict))  # Output: {'a': 1, 'b': 2, 'c': 3}

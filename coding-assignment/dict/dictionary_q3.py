# Write a function to invert a dictionary (swap keys and values).

def invert_dict(d):
    return {v: k for k, v in d.items()}

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(invert_dict(my_dict))  # Output: {1: 'a', 2: 'b', 3: 'c'}

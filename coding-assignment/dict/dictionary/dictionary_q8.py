# Write a function to get all values from a dictionary.

def get_values(d):
    return list(d.values())

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(get_values(my_dict))  # Output: [1, 2, 3]

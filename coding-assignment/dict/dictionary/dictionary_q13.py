# Write a function to find the minimum value in a dictionary.

def min_value(d):
    return min(d.values())

# Test the function
my_dict = {"a": 5, "b": 2, "c": 3}
print(min_value(my_dict))  # Output: 2

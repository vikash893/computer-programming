# Write a function to filter a dictionary by values that are greater than a given number.

def filter_by_value(d, threshold):
    return {k: v for k, v in d.items() if v > threshold}

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(filter_by_value(my_dict, 2))  # Output: {'c': 3}

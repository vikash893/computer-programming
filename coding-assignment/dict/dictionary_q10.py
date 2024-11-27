# Write a function to sort a dictionary by value.

def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Test the function
my_dict = {"a": 3, "b": 1, "c": 2}
print(sort_by_value(my_dict))  # Output: {'b': 1, 'c': 2, 'a': 3}

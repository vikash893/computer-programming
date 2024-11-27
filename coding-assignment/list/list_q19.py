# Write a function to check if one list is a sublist of another.

def is_sublist(lst1, lst2):
    return all(item in lst2 for item in lst1)

# Test the function
print(is_sublist([1, 2], [1, 2, 3]))  # Output: True
print(is_sublist([1, 4], [1, 2, 3]))  # Output: False

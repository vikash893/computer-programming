# Write a function to remove an element from a list by value.

def remove_element(lst, elem):
    return [item for item in lst if item != elem]

# Test the function
print(remove_element([1, 2, 3, 4], 3))  # Output: [1, 2, 4]

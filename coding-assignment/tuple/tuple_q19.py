# Write a function to check if an element exists in a tuple

def element_exists(t, elem):
    return elem in t

# Test the function
print(element_exists((1, 2, 3), 2))  # Output: True
print(element_exists((1, 2, 3), 4))  # Output: False

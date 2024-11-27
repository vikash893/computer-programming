# Write a function to add an element to a tuple.

def add_element(t, elem):
    return t + (elem,)

# Test the function
print(add_element((1, 2, 3), 4))  # Output: (1, 2, 3, 4)

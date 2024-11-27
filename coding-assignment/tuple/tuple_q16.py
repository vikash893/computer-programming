# Write a function to remove an element from a tuple.

def remove_element(t, elem):
    return tuple(x for x in t if x != elem)

# Test the function
print(remove_element((1, 2, 3), 2))  # Output: (1, 3)

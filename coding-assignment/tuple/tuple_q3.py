# Write a function to unpack a tuple into variables.

def unpack_tuple(t):
    a, b, c = t
    return a, b, c

# Test the function
print(unpack_tuple((1, 2, 3)))  # Output: (1, 2, 3)

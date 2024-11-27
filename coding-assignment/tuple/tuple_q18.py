# Write a function to slice a tuple.

def slice_tuple(t, start, end):
    return t[start:end]

# Test the function
print(slice_tuple((1, 2, 3, 4, 5), 1, 4))  # Output: (2, 3, 4)

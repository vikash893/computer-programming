# Write a function to convert a tuple to a string.

def tuple_to_string(t):
    return ''.join(map(str, t))

# Test the function
print(tuple_to_string((1, 2, 3)))  # Output: '123'

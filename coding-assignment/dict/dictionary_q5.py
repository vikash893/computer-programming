# Write a function to check if a dictionary is empty.

def is_empty(d):
    return not bool(d)

# Test the function
print(is_empty({}))  # Output: True
print(is_empty({"a": 1}))  # Output: False

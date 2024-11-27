# Write a function to find duplicates in a tuple.

def find_duplicates(t):
    return [item for item in set(t) if t.count(item) > 1]

# Test the function
print(find_duplicates((1, 2, 2, 3, 3, 3)))  # Output: [2, 3]

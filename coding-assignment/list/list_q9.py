# Write a function to remove duplicates from a list.

def remove_duplicates(lst):
    return list(set(lst))

# Test the function
print(remove_duplicates([1, 2, 2, 3, 3, 3]))  # Output: [1, 2, 3]

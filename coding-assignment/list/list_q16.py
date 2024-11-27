# Write a function to find the intersection of two lists.

def intersection(lst1, lst2):
    return [item for item in lst1 if item in lst2]

# Test the function
print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]

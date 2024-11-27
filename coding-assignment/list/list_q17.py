# Write a function to find the union of two lists.

def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

# Test the function
print(union([1, 2, 3], [3, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# Write a function to find the difference between two lists.

def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

# Test the function
print(difference([1, 2, 3], [2, 3, 4]))  # Output: [1]

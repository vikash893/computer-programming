# Write a function to find common elements in two lists.

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Test the function
print(common_elements([1, 2, 3], [3, 4, 5]))  # Output: [3]

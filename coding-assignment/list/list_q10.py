# Write a function to rotate a list by a given number of positions.

def rotate_list(lst, n):
    return lst[-n:] + lst[:-n]

# Test the function
print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

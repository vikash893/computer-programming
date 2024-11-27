# Write a function to convert a tuple of tuples to a list of lists.

def tuple_of_tuples_to_list_of_lists(t):
    return [list(x) for x in t]

# Test the function
print(tuple_of_tuples_to_list_of_lists(((1, 2), (3, 4))))  # Output: [[1, 2], [3, 4]]

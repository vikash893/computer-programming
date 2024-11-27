# Write a function to flatten a nested list.

def flatten_list(nested_lst):
    flat_list = []
    for sublist in nested_lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list

# Test the function
print(flatten_list([[1, 2], [3, 4], [5, 6]]))  # Output: [1, 2, 3, 4, 5, 6]

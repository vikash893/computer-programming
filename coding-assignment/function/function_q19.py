# Write a function to check if a list is sorted in ascending order.

def is_sorted(lst):
    return lst == sorted(lst)

# Test the function
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2, 4]))  # Output: False

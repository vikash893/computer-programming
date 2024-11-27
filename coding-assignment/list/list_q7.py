# Write a function to find the second largest number in a list

def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

# Test the function
print(second_largest([1, 2, 3, 4]))  # Output: 3

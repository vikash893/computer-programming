# Write a function to find the maximum value in a list.

def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

# Test the function
print(find_max([1, 2, 3, 4]))  # Output: 4

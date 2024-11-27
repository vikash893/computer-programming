# Write a function to find the minimum value in a list.

def find_min(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

# Test the function
print(find_min([1, 2, 3, 4]))  # Output: 1

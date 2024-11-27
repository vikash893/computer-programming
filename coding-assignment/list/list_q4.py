# Write a function to calculate the sum of elements in a list.

def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
print(sum_list([1, 2, 3, 4]))  # Output: 10

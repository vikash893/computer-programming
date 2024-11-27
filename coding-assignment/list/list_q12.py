# Write a function to find the missing number in a list of integers from 1 to n.

def find_missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)

# Test the function
print(find_missing_number([1, 2, 4, 5], 5))  # Output: 3

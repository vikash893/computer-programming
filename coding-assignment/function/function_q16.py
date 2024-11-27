# Write a function to find the length of a list without using the len() function

def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# Test the function
print(list_length([1, 2, 3, 4]))  # Output: 4

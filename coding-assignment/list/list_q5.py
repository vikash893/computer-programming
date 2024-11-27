# Write a function to count the occurrences of a specific element in a list

def count_occurrences(lst, elem):
    count = 0
    for item in lst:
        if item == elem:
            count += 1
    return count

# Test the function
print(count_occurrences([1, 2, 2, 3, 3, 3], 2))  # Output: 2

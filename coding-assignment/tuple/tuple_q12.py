# Write a function to count the occurrences of an element in a tuple.

def count_in_tuple(t, elem):
    return t.count(elem)

# Test the function
print(count_in_tuple((1, 2, 2, 3), 2))  # Output: 2

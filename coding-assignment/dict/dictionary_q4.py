# Write a function to count the frequency of items in a list and return a dictionary.

def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Test the function
my_list = [1, 2, 2, 3, 3, 3]
print(count_frequency(my_list))  # Output: {1: 1, 2: 2, 3: 3}

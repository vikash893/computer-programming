# Write a function to find the key with the maximum value in a dictionary.

def max_value_key(d):
    return max(d, key=d.get)

# Test the function
my_dict = {"a": 5, "b": 10, "c": 3}
print(max_value_key(my_dict))  # Output: b

# Write a function to convert a dictionary to a list of tuples.

def dict_to_tuples(d):
    return list(d.items())

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_tuples(my_dict))  # Output: [('a', 1), ('b', 2), ('c', 3)]

# Write a function to merge two dictionaries.
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

# Test the function
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}

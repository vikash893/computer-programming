# Write a function to calculate the average value of a dictionary.

def average_value(d):
    return sum(d.values()) / len(d) if d else 0

# Test the function
my_dict = {"a": 1, "b": 2, "c": 3}
print(average_value(my_dict))  # Output: 2.0

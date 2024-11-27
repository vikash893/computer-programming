# Write a function to generate a list of squares of numbers from 1 to n.

def list_of_squares(n):
    return [i**2 for i in range(1, n + 1)]

# Test the function
print(list_of_squares(5))  # Output: [1, 4, 9, 16, 25]

# Write a function to find the sum of digits of a number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Test the function
print(sum_of_digits(1234))  # Output: 10

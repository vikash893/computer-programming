# Write a function to calculate the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
print(gcd(48, 18))  # Output: 6

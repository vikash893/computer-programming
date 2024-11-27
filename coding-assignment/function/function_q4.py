# Write a function to print the Fibonacci sequence up to a given number.

def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Test the function
print(fibonacci(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

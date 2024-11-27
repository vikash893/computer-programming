# Count the number of distinct substrings of a string.
def count_distinct_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return len(substrings)

# Example:
print(count_distinct_substrings("abc"))  # Output: 6

# Check if one string is a subsequence of another.
def is_subsequence(s, t):
    it = iter(t)
    return all(c in it for c in s)

# Example:
s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))  # Output: True

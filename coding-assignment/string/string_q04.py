# Determine if two strings are anagrams.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example:
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # Output: True

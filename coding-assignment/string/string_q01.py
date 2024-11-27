#  Check if Strings are Rotations of Each Other
def are_rotations(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

# Example:
s1 = "ABCD"
s2 = "CDAB"
print(are_rotations(s1, s2))  # Output: True

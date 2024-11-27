# Generate all permutations of a given string.
from itertools import permutations

def find_permutations(s):
    return ["".join(p) for p in permutations(s)]

# Example:
print(find_permutations("abc"))  
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

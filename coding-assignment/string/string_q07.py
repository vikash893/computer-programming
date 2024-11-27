# Group anagrams from a list of strings.
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[tuple(sorted(word))].append(word)
    return list(anagrams.values())

# Example:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

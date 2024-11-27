# Write a function to find the longest substring without repeating characters.
def longest_unique_substring(s):
    seen = {}
    start = max_length = 0
    
    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test the function
print(longest_unique_substring("abcabcbb"))  # Output: 3 (abc)

# Implement basic string compression using counts of repeated characters.
def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    compressed = ''.join(compressed)
    return compressed if len(compressed) < len(s) else s

# Example:
print(compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"

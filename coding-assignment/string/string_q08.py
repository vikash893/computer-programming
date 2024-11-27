# Find the longest palindromic substring in a string.
def longest_palindromic_substring(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        temp = expand(i, i)
        if len(temp) > len(longest):
            longest = temp
        # Even-length palindrome
        temp = expand(i, i + 1)
        if len(temp) > len(longest):
            longest = temp
    return longest

# Example:
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"

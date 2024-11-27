# Given an integer n, generate the nth term in the "count-and-say" sequence.
def count_and_say(n):
    s = "1"
    for _ in range(n - 1):
        next_seq = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                next_seq += str(count) + s[i - 1]
                count = 1
        next_seq += str(count) + s[-1]
        s = next_seq
    return s


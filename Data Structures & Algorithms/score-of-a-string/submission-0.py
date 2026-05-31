class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for pos in range(len(s) - 1):
            sum += abs(ord(s[pos]) - ord(s[pos + 1]))
        return sum

        
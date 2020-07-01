class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while j < len(s) and i < len(t):
            if t[i] == s[j]:
                j += 1
            i += 1

        return True if j == len(s) else False


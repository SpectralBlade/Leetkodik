from collections import Counter

class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in range(len(s)):
            if c.get(s[i]) == 1:
                return i
        return -1
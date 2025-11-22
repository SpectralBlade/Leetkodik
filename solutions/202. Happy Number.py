class Solution(object):
    def isHappy(self, n: int) -> bool:
        results = set()
        while n != 1:
            if n in results:
                return False
            results.add(n)
            x = 0
            for k in str(n):
                x += int(k)**2
            n = x
        return True
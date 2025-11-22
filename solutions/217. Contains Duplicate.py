class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        res = set()
        for k in nums:
            if k in res:
                return True
            res.add(k)
        return False
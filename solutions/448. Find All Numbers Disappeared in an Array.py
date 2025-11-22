class Solution(object):
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums2 = set(nums)
        return [x for x in range(1, len(nums)+1) if x not in nums2]
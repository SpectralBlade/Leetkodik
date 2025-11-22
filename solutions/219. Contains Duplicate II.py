class Solution(object):
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums2 = {}
        for n, i in enumerate(nums):
            if i in nums2 and n - nums2[i] <= k:
                return True
            nums2[i] = n
        return False
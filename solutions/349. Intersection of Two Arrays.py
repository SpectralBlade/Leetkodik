class Solution(object):
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums2 = (set(nums2))
        nums3 = set()
        for i in nums1:
            if i in nums2:
                nums3.add(i)
        return list(nums3)
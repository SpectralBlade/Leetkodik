class Solution(object):
    def longestConsecutive(self, nums: list[int]) -> int:
        nums2 = set(nums)
        maxlen = 0

        for num in nums2:
            if num - 1 not in nums2:
                current_num = num
                current_len = 1
                while current_num + 1 in nums2:
                    current_num += 1
                    current_len += 1
                maxlen = max(maxlen, current_len)

        return maxlen

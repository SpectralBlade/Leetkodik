class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1

        re = k
        for i in range(len(count) - 1, -1, -1):
            re -= count[i]
            if re <= 0:
                return i + min_val

        return -1
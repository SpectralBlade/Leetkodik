class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum1 = len(nums) * (len(nums) + 1) // 2
        sum2 = sum(nums)
        return sum1 - sum2

# Победа
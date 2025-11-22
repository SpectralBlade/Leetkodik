class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in num_map:
                return [num_map[num2], i]
            num_map[num] = i
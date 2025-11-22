class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        p_sum = 0
        sum_freq = {0: 1}

        for num in nums:
            p_sum += num
            if p_sum - k in sum_freq:
                count += sum_freq[p_sum - k]
            sum_freq[p_sum] = sum_freq.get(p_sum, 0) + 1

        return count
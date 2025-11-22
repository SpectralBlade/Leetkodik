# Данный персонаж занял больше времени, чем остальные...

class Solution(object):
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ILoveSamir = {}
        for n in nums:
            ILoveSamir[n] = ILoveSamir.get(n, 0) + 1
        ILoveSamir = sorted(ILoveSamir.items(), key=lambda item: item[1], reverse=True)
        return [match[0] for match in ILoveSamir[:k]]

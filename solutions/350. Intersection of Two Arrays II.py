class Solution(object):
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ruletka = {}
        kazik = {}

        for num in nums1:
            ruletka[num] = ruletka.get(num, 0) + 1
        for num in nums2:
            kazik[num] = kazik.get(num, 0) + 1

        result = []
        for num in ruletka:
            if num in kazik:
                count = min(ruletka[num], kazik[num])
                result.extend([num] * count)

        return result
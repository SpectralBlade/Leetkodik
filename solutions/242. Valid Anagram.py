class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        kazik = {}
        ruletka = {}

        for i in range(len(s)):
            kazik[s[i]] = kazik.get(s[i], 0) + 1
            ruletka[t[i]] = ruletka.get(t[i], 0) + 1

        return kazik == ruletka
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        kazik_s_gusyami = defaultdict(list)
        for s in strs:
            n = ''.join(sorted(s))
            kazik_s_gusyami[n].append(s)
        return list(kazik_s_gusyami.values())
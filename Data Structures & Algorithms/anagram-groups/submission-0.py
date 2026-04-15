class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        for st in strs:
            st_cnt = Counter(st)
            st_cnt_frz = frozenset(st_cnt.items())
            ana_map[st_cnt_frz].append(st)
        return list(ana_map.values())
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        subs_sizes = []
        seen = set()
        start = 0
        for i in range(len(s)):
            c = s[i]
            count[c] -= 1
            seen.add(c)
            if count[c] == 0:
                seen.remove(c)
                if not seen:
                    subs_sizes.append(i-start+1)
                    start = i + 1
        
        return subs_sizes
            
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_substring = ""
        t_count = Counter(t)
        subs_count = defaultdict(int)
        completed = set()
        tail = 0
        for i in range(len(s)):
            if s[i] not in t_count:
                continue
            subs_count[s[i]] += 1
            while tail < i and (s[tail] not in t_count or subs_count[s[tail]] > t_count[s[tail]]):
                subs_count[s[tail]]-=1
                tail+=1
            if subs_count[s[i]] == t_count[s[i]]:
                completed.add(s[i])
                if len(completed) == len(t_count) and (not shortest_substring or i-tail+1 < len(shortest_substring)):
                    shortest_substring = s[tail:i+1]
        return shortest_substring
            
                

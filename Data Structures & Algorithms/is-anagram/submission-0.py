class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_freqs = Counter(s)
        t_char_freqs = Counter(t)
        for k, v in s_char_freqs.items():
            if k not in t_char_freqs or v != t_char_freqs[k]:
                return False
        return True
        
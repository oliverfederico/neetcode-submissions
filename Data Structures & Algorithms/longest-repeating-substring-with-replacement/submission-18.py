class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = [0]*26
        for c in s:
            freqs[ord(c)-ord('A')]+=1
        f_max = 0
        c_max = None
        for i in range(26):
            if freqs[i] > f_max:
                f_max = freqs[i]
                c_max = chr(ord('A')+i)
        longest = 0
        for i in range(26):
            c_target = chr(ord('A') + i)
            current_k = k
            slow = fast = 0
            while fast < len(s):
                if s[fast] != c_target:
                    if current_k > 0:
                        current_k -= 1
                    else:
                        while s[slow] == c_target:
                            slow += 1
                        slow += 1
                fast += 1
                longest = max(longest, fast - slow)
        return longest
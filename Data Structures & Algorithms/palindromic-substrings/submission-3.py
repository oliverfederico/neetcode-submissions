class Solution:
    def countSubstrings(self, s: str) -> int:
        padded_s = '#' + '#'.join(s) + '#'
        radii = [0 for _ in range(len(padded_s))]
        count = 0
        center = 0
        right_boundry = 0

        for i in range(len(padded_s)):
            if i > right_boundry:
                radius = 0
            else:
                mirror = center - (i - center)
                radius = min(radii[mirror], right_boundry-i)
            l, r = i - radius - 1, i + radius + 1 
            while 0 <= l and r < len(padded_s) and padded_s[l] == padded_s[r]:
                l -=1
                r +=1
                radius+=1
            radii[i]= radius
            if i + radius > right_boundry:
                center = i
                right_boundry = radius + i
            count += (radius + 1) // 2
    
        return count
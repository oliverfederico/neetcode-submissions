class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        b_map = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in b_map:
                if not st or st.pop() != b_map[b]:
                    return False
            else:
                st.append(b)
        return len(st) == 0


        
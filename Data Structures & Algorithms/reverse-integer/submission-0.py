class Solution:
    # 12 -> 01100 21 -> 10101
    def reverse(self, x: int) -> int:
        pos_x = x if x >= 0 else -x
        str_x = str(pos_x)
        rev_str_x = "".join(reversed(str_x))
        rev_x = int(rev_str_x) if x >= 0 else -int(rev_str_x)
        if -2**31 <= rev_x <= 2**31-1:
            return rev_x
        return 0
        
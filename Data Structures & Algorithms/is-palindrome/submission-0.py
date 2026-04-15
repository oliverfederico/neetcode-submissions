class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = set(list("qwertyuiopasdfghjklzxcvbnm1234567890"))
        s = s.lower()
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] not in valid_chars:
                low +=1
            elif s[high] not in valid_chars:
                high -= 1
            elif s[low] != s[high]:
                return False
            else:
                low +=1
                high -=1

        return True
        
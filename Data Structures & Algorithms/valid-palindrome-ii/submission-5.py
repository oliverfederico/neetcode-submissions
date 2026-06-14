class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # Helper function to check if a standard string is a perfect palindrome
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Mismatch found. We have exactly two choices: 
                # 1. Skip the left character (check s[l+1 : r])
                # 2. Skip the right character (check s[l : r-1])
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            
            l += 1
            r -= 1
            
        return True
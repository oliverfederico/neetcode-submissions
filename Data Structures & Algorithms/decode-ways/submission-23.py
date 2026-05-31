class Solution:
    def numDecodings(self, s: str) -> int:
        # Base case: empty string or starting with '0' is invalid
        if not s or s[0] == '0':
            return 0
        
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 1 
        prev1 = 1 
        
        for i in range(1, len(s)):
            curr = 0
            
            # 1. Single digit check (1-9)
            if s[i] != '0':
                curr += prev1
                
            # 2. Double digit check (10-26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2
                
            # Shift our variables forward for the next iteration
            prev2 = prev1
            prev1 = curr
            
        return prev1
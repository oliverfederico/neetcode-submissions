from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # 1. Create count maps for s1 and the first window in s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)]) # Count for the first window
        
        # 2. Check the first window
        if s1_count == window_count:
            return True
            
        # 3. Slide the window one character at a time
        # We start from the character *after* the first window ends
        for i in range(len(s1), len(s2)):
            
            # 'i' is the new character *entering* the window (right side)
            new_char = s2[i]
            window_count[new_char] += 1
            
            # 'i - len(s1)' is the old character *leaving* the window (left side)
            old_char = s2[i - len(s1)]
            
            # Remove the old_char from the window's count
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char] # Clean up the counter
                
            # 4. Check for a match after each slide
            if s1_count == window_count:
                return True
                
        # 5. If we finish the loop, no match was found
        return False
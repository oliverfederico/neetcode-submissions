from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Identify which half is sorted
            # Case 1: Left half [l...m] is sorted
            if nums[l] <= nums[m]:
                # Check if target is within this sorted left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Case 2: Right half [m...r] is sorted
            else:
                # Check if target is within this sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1
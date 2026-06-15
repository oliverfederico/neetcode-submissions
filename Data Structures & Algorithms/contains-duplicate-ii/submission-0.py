class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        in_window = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in in_window:
                return True
            if len(in_window) >= k:
                in_window.remove(nums[i-len(in_window)])
            in_window.add(num)
        return False
            

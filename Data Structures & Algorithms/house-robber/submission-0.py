class Solution:
    # so we would want to rob ever other house unless not robbing two houses in a row allows us to earn more
    # we can use dp by making a cumulative sum, but if we do that how do we know when to switch pattern
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums[2] += nums[0]
        if len(nums) > 3:
            for i in range(3, len(nums)):
                nums[i] += max(nums[i-2], nums[i-3])
        
        return max(nums[-1], nums[-2])

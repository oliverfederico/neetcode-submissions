class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        # Standard linear House Robber logic wrapped in a helper
        def helper(houses):
            rob1, rob2 = 0, 0
            for num in houses:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # Scenario 1: Exclude the last house (nums[:-1])
        # Scenario 2: Exclude the first house (nums[1:])
        return max(helper(nums[:-1]), helper(nums[1:]))
class Solution:
    # will be equal when one half == half of sum 
    # problem becomes given a number can you tell me if arr can make that number 
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 or len(nums) == 1:
            return False
        target = total // 2
        if max(nums) > target:
            return False

        checked = [set() for _ in range(len(nums))]

        def dfs(goal, i) -> bool:
            if goal == 0:
                return True
            if goal < 0 or i == len(nums):
                return False
            if goal in checked[i]:
                return False
            checked[i].add(goal)
            return dfs(goal-nums[i],i+1) | dfs(goal, i+1)

        
        return dfs(target,0)
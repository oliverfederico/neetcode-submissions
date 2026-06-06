class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_range = nums[0]
        max_range = 0
        jumps = 0
        for i in range(1, len(nums)):
            max_range = max(max_range, i + nums[i])
            if i == curr_range or i == len(nums) - 1:
                curr_range = max_range
                max_range = 0
                jumps += 1
        return jumps
class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_range = 0
        max_range = 0
        jumps = 0
        for i in range(len(nums)):
            max_range = max(max_range, i + nums[i])
            if i == curr_range and i < len(nums)-1:
                curr_range = max_range
                max_range = 0
                jumps += 1
        return jumps
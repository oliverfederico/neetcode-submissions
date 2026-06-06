class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_idx = len(nums) -1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= target_idx:
                target_idx = i
        return target_idx == 0
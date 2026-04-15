class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_idxs = {}
        for i, n in enumerate(nums):
            if n in sum_idxs:
                return [sum_idxs[n], i]
            sum_idxs[target-n] = i
        
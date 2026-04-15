class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            curr_i = (low + high)//2
            if nums[curr_i] == target:
                return curr_i
            elif nums[curr_i] < target:
                low = curr_i+1
            else:
                high = curr_i
        return -1
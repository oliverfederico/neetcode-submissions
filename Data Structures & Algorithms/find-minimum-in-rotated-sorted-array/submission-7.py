# binary search, search for the min == search for max == search for the "boundry" (end of original array)
# left, right, curr_min, if 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            h = (left + right)//2
            if nums[h] > nums[right]:
                left = h + 1
            else:
                right = h
        return nums[left]

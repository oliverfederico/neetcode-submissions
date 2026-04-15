class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        low = 0
        high = len(nums)-1
        while low < high:
            while low < high and nums[high] == val:
                high -= 1
            if nums[low] == val:
                nums[low] = nums[high]
                nums[high] = val
            low +=1
        return high if nums[high] == val else high + 1

        
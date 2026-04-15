class Solution:
    # ignore position
    # brute is iterate with set, o(n) space and time
    # 1010 1110
    # xor all, from l to r, 
    # 0 x 1, 1 x 11, 11 x 0, 00 x 10, 10 x 00
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = nums[0]
        fast = nums[fast]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
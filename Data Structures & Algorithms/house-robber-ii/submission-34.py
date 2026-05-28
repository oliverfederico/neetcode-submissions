class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        if len(nums) == 4:
            return max(nums[0]+nums[2], nums[1] + nums[3])
        # for i in range(len(nums)-2):
        #     if nums[i-3] > nums[i-2] and nums[i-3] > nums[i-1]:
        #         nums[i-2] = nums[i-3]
        #         nums[i-3] = 0 
        #     nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        # print(nums)
            
        # return max(nums[-3], nums[-4])
        # for i in range(len(nums)):
        #     nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        # print(nums)
        # if nums[0] == nums[1]:
        #     # we used 0 + -2 over -1 + 1
        #     if nums[-1] == nums[-2]:
        #         # we used -2 + -4 over -1 + -3
        # else:
            
        # return min(nums[-1], nums[-2], nums[-3])
        rob1 = nums[-2]
        rob2 = nums[-1]
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            print(rob2)
        if rob1 != rob2:
            if nums[-1] > nums[-2] + nums[0]:
                return rob2 - nums[-1]
            else:
                if nums[-2] > nums[-1]:
                    if nums[-3] > nums[-2] and nums[-3] > nums[0]:
                        return rob2 - nums[-1]
                    return(rob1 - nums[-2])
                return rob1 - nums[-2]
        return rob2


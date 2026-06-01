class Solution:
    # 1,2,3,4 -> 1, 1*2, 1*2*3, 1*2*3*4 -> 2, 2*3, 2*3*4 -> 3, 3*4 -> 4
    def maxProduct(self, nums: List[int]) -> int:
        max_p = nums[0]
        l = -1
        for i in range(len(nums)):
            max_p = max(max_p, nums[i])
            if nums[i] == 0:
                l = i
            else:
                for j in range(i-1, l, -1):
                    nums[j] *= nums[i]
                    max_p = max(max_p, nums[j])
        return max_p 
            

            

        
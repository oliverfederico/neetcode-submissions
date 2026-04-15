class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_idx = -1
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_idx != -1:
                    return [0] * len(nums)
                zero_idx = i
            else:
                prod *= nums[i]
        prod_arr = [prod] * len(nums)
        for i in range(len(nums)):
            if i != zero_idx: 
                if zero_idx == -1:
                    prod_arr[i] = prod // nums[i]
                else:
                    prod_arr[i] = 0
        return prod_arr


        
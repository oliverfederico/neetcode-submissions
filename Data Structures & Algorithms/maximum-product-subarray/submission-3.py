class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = nums[0]
        max_p = 1
        min_p = 1
        for num in nums:
            min_t = min_p * num
            max_t = max_p * num
            min_p = min(min_t, max_t, num)
            max_p = max(min_t, max_t, num)
            p = max(p, max_p)
            # if num < 0:
            #     if min_p < 0:
            #         max_p = max(max_p, min_p * num)
            #     else:
            #         min_p = min(min_p, max_p * num)
            # if max_p < 0:
        return p

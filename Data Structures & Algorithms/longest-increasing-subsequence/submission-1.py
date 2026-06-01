class Solution:
    # bottom up dp, we store the start and length of longest subseq for each num,  we iterate left to right, 
    # for any given number we want to know the longest subseq to that left of it that ends lower than it.
    # brute force: we go throught each left num and find the longest where num is lower than i
    # this would be n^2 with n space
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]

        for i in range(1,len(nums)):
            if tails[-1] < nums[i]:
                tails.append(nums[i])
            elif tails[-1] > nums[i]:
                l, r = 0, len(tails)
                while l < r:
                    m = (l+r)//2
                    if tails[m] >= nums[i]:
                        r = m
                    elif tails[m] < nums[i]:
                        l = m + 1
                tails[l] = nums[i]
            
        return len(tails)
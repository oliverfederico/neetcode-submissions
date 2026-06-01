class Solution:
    # bottom up dp, we store the start and length of longest subseq for each num,  we iterate left to right, 
    # for any given number we want to know the longest subseq to that left of it that ends lower than it.
    # brute force: we go throught each left num and find the longest where num is lower than i
    # this would be n^2 with n space
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)

        for i in range(len(nums)):
            max_l = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_l = max(max_l, lengths[j])
            lengths[i] = max_l + 1
        return max(lengths)
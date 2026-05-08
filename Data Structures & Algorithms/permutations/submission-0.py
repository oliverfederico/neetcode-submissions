class Solution:
    # how do we only visit each num once per perm
    # store the remaining nums, constant access, iteration, removal and addition
    # we check
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def dfs(subList):
            # stop when perm has all nums
            if len(subList) == len(nums):
                permutations.append(subList.copy())
                return
            
            for num in nums:
                if num not in subList:
                    subList.append(num)
                    dfs(subList)
                    subList.pop()
            
        dfs([])
        return permutations

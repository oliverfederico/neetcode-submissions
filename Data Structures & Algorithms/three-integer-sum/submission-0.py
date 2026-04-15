class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        targets = defaultdict(list)
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j:
                    targets[-a-b].append([i,j])
        result = set()
        for k, c in enumerate(nums):
            if c in targets:
                for pair in targets[c]:
                    if k not in pair:
                        a, b = pair
                        result.add(tuple(sorted([nums[a], nums[b], c])))
        return list(result)
        


        
class Solution:
    # result can be thought of a tree where each node is a subset or path is subset so no two paths the same
    # traverse by adding num if count > 0 or remaining other nums
    # [] -> [1], [2] -> [1,1] [1,2] -> [1,1,2]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        counter = Counter(nums)
        for num, count in counter.items():
            head = len(subsets)
            for i in range(count):
                for j in range(head):
                    subsets.append(subsets[head*i+j].copy())
                    subsets[-1].append(num)
        
        return subsets
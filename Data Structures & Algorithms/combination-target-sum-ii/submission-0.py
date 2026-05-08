class Solution:
    # we can only use a candidate one so we don't recurse on j==i a second time
    # we can't have duplicate combinations so we either check for duplicate or we avoid 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def dfs(i, subcomb, total):
            if total == target:
                combinations.append(subcomb.copy())
                return
            
            for j in range(i, len(candidates)):
                # stop early
                if total + candidates[j] > target:
                    return
                # don't recurse in the same valued candidates
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                subcomb.append(candidates[j])
                dfs(j+1, subcomb, total+candidates[j])
                subcomb.pop()
        
        dfs(0, [], 0)

        return combinations
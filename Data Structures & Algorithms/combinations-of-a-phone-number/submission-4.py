class Solution:
    # dfs
    # iterative 
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numpad = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        combinations = []
        dl = len(digits)
        def dfs(i, comb):
            if i == dl:
                combinations.append(comb)
                return
            for c in numpad[digits[i]]:
                dfs(i+1, comb+c)
        dfs(0,"")
        return combinations

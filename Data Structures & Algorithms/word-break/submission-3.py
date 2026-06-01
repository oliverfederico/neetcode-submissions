class Solution:
    # iterate through string until we match, then reset left pointer, backtrack if we reach EoS.
    # or we can continue iterating until we reach EoS and collect all words we have matched
    # then we can use them as starting points for next iteration,
    # if we fail to match from a given point we mark that as failed so we don't revisit
    # should we do this in a bf or df manner - it doesn't really make a differnce - dfs might be easier
    # we will use each letter as a starting point once in worse case and iterate over remaining so O(n^2*t) wher t is dict size
    # we can improve this to O(n*m*t) where m in length of largest dict word by stopping iter early
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        checked = [False] * len(s)

        max_l = max(len(word) for word in wordDict)

        wordSet = set(wordDict)

        def dfs(i: int) -> bool:
            if i == len(s):
                return True
            if checked[i]:
                return False
            for j in range(i, min(i+max_l,len(s))):
                if s[i:j+1] in wordSet and dfs(j+1):
                    return True
            checked[i] = True
            return False
                    

        return dfs(0)
        
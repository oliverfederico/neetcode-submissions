class Solution:
    # min k will be 1 if sum(piles) <= h
    # of
    # max k will be max(piles) if len(piles) == h
    # so 0 < k <= max(piles)
    # BF: 
    # minimise k such that sum(ceiling(piles[i]//k))<=h => ceil(pile[0]/k) + ceil(pile[1]/k) + ... <= h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if sum(piles) <= h:
            return 1
        elif len(piles) == h:
            return max(piles)
        else:
            result = max(piles)
            l = 1
            t = result
            while l <= t:
                m = (t + l) // 2
                val = sum(map(lambda x : math.ceil(x/m),piles))
                if val <= h:
                    result = m
                    t = m -1
                else:
                    l = m + 1
            return result

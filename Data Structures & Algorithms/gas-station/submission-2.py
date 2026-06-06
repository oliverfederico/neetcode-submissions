class Solution:
    # 10 9 -> 
    # [ 0, 0,  1, 0]
    # [-1, 0, -1, 3]
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1




        return res 
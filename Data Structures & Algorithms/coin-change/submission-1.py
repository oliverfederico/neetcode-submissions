class Solution:
    # amount of 0 return 0
    # counts = [amount] return 1
    # sort coins as we aren't told they are ordered
    # ignore all coins larger than amount 
    # prime factors of coin values and amount 
    # 1100, 1010, 0101, 0001 
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        if coins[0] > amount:
            return -1
        # while coins and coins[-1] > amount:
        #     coins.pop()

        # counts = {}
        # for a in range(coins[0],amount):
        #     for c in reversed(coins):
        #         if a % c == 0:
        #             counts[a] = a//c
        #             break
        


        visited = set()
        counts = [amount]
        num = 1
        while counts:
            new_counts = []
            for count in counts:
                for c in coins:
                    if count-c == 0:
                        return num
                    if count-c < coins[0]:
                        break 
                    if count - c not in visited:
                        visited.add(count-c)
                        new_counts.append(count-c)
            counts = new_counts
            num+=1
        
        return -1


            

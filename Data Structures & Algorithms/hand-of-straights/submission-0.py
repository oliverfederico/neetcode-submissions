class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        heads = [hand[0]]
        lens = [1]
        curr = 1
        while curr < len(hand):
            h_idx = 0
            while h_idx < len(heads):
                if lens[h_idx] < groupSize and hand[curr] == heads[h_idx] + 1:
                    heads[h_idx] = hand[curr]
                    lens[h_idx] += 1
                    break
                if h_idx == len(heads) - 1 and len(heads) < len(hand) // groupSize:
                    heads.append(hand[curr])
                    lens.append(1)
                    break
                h_idx += 1
            if h_idx == len(heads):
                return False
            curr += 1
        return True
                
                

                
            


            

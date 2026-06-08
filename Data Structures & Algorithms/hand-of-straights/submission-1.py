class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        for card in hand:
            start = card
            while counter[start - 1]:
                start -= 1
            while counter[start] > 0:
                for i in range(start, start + groupSize):
                    if counter[i] == 0:
                        return False
                    counter[i] -= 1
            
        return True
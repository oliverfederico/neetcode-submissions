class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) -1
        while low < high:
            pair_total = numbers[low] + numbers[high]
            if pair_total == target:
                return [low+1, high+1]
            if pair_total < target:
                low += 1
            else:
                high -= 1
        

        
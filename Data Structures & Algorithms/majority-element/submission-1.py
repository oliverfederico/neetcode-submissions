class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        maj = nums[0]
        for num in nums:
            freqs[num] += 1
            if freqs[num] > freqs[maj]:
                maj = num
        return maj
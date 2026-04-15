class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            freqs[count].append(num)
        top_k = []
        while len(top_k) < k:
            top_k += freqs.pop()
        return top_k

        
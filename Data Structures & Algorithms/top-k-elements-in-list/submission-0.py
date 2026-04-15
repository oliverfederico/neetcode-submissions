class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs_dict = Counter(nums)
        freqs_srtd = sorted(list(freqs_dict.items()), key=lambda x: x[1])
        top_k = []
        for i in range(k):
            top_k.append(freqs_srtd[-i-1][0])
        return top_k
        
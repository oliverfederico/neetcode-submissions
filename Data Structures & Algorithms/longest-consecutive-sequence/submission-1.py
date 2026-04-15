class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seqs = {}
        max_seq = 0
        for num in nums:
            if num not in seqs:
                if num+1 in seqs and num-1 in seqs:
                    r_len = seqs[num + seqs[num + 1]] 
                    l_len = seqs[num - seqs[num - 1]]
                    seqs[num + seqs[num + 1]] += 1 + l_len
                    seqs[num - seqs[num - 1]] += 1 + r_len
                    seqs[num] = 0
                elif num +1 in seqs:
                    r_len = seqs[num + seqs[num + 1]] 
                    seqs[num + seqs[num + 1]] += 1
                    seqs[num] = r_len + 1
                elif num - 1 in seqs:
                    l_len = seqs[num - seqs[num - 1]]
                    seqs[num - seqs[num - 1]] += 1
                    seqs[num] = l_len + 1
                else:
                    seqs[num] = 1
            
        return max(list(seqs.values()))


            
                
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(min(len(word1), len(word2))):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.append(word1[min(len(word1), len(word2)):len(word1)])
        merged.append(word2[min(len(word1), len(word2)):len(word2)])
        return "".join(merged)
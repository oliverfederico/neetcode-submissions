class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # 1. Build the Trie: O(m * t) time
        trie = Trie()
        max_l = 0
        for word in wordDict:
            trie.insert(word)
            max_l = max(max_l, len(word))

        # 2. Initialize DP array
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        # 3. Bottom-Up DP: O(n * t) time
        for i in range(n - 1, -1, -1):
            node = trie.root  # Start at the root for index 'i'
            
            for j in range(i, min(n, i + max_l)):
                char = s[j]
                
                # If the character isn't a valid path, break early!
                # This string prefix doesn't exist in the dictionary at all.
                if char not in node.children:
                    break 
                
                # Move down the Trie
                node = node.children[char]
                
                # If we found a valid word AND the remaining substring is valid
                if node.is_word and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]
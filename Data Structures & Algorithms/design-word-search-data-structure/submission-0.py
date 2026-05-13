class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word: str) -> bool:
        backup = self.trie
        curr = self.trie
        for i in range(len(word)):
            if word[i] == '.':
                for k in curr.keys():
                    if k != '*': 
                        self.trie = curr[k]
                        if self.search(word[i+1:]):
                            self.trie = backup
                            return True
                self.trie = backup
                return False
            if word[i] not in curr:
                return False
            curr = curr[word[i]]
        return '*' in curr

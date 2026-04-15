from queue import Queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = set()
        queue = Queue()
        max_len = 0
        for char in s:
            if char in sub_str:
                while queue:
                    head = queue.get()
                    sub_str.remove(head)
                    if head == char:
                        break
            sub_str.add(char)
            queue.put(char)
            max_len = max(max_len, len(sub_str))

        return max_len

        
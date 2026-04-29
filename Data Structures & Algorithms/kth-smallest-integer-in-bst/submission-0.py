# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visit = [root]
        visited = []
        count = 0
        while visit or visited:
            if visit:
                node = visit.pop()
                while node.left:
                    visited.append(node)
                    node = node.left
            else:
                node = visited.pop()
            count +=1
            if count == k:
                return node.val
            if node.right:
                visit.append(node.right)


        # c = 0
        # def n_count(node):
        #     if node.left:
        #         n_count(node.left)
        #     c+=1
        #     if c == k:
        #         return node.val
        #     if node.right:
        #         n_count(node.right)
        # return n_count(root)
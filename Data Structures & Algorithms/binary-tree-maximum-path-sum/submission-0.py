# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def pathSum(node):
            l = lm = r = rm = float('-inf')
            if node.left:
                l, lm = pathSum(node.left)
            if node.right:
                r, rm = pathSum(node.right)
            p = node.val
            if max(l,r) > 0:
                p += max(l,r)
            return (p, max(p, l + r + node.val, rm, lm))
        
        return int(pathSum(root)[1])
            
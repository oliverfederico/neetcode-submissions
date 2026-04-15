# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        to_visit = [(root, 1)]
        max_depth = 0
        while to_visit:
            curr, depth = to_visit.pop()
            if curr.right:
                to_visit.append((curr.right, depth+1))
            if curr.left:
                to_visit.append((curr.left, depth+1))
            max_depth = max(max_depth, depth)
        return max_depth


        
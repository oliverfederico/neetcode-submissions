# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def diaHelper(node, depth):
            ldepth = 0
            rdepth = 0
            if node.left:
                ldepth = diaHelper(node.left, depth+1)
            if node.right:
                rdepth = diaHelper(node.right, depth+1)
            path = depth + ldepth + rdepth - min(depth, ldepth, rdepth)
            self.diameter = max(self.diameter, path)
            return max(ldepth,rdepth) + 1
        diaHelper(root, 0)
        return self.diameter

        
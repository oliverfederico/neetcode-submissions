# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # make it so p < q (symetrically)
    # if curr == p or q then lca = curr return
    # if p < curr < q then lca = curr return
    # if curr < p then curr = curr.right
    # else curr = curr.left
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        while root != p and root != q and (p.val > root.val or q.val < root.val):
            if root.val > q.val:
                root = root.left
            else:
                root = root.right
        return root
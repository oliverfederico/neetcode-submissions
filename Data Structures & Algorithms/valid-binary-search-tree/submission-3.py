# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # top down vs bottom up
    # bottom up, store, lowest and highest value, as we move up we compare based on if we move right or left
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        visit = deque([(root, float("-inf"), float("inf"))])
        while visit:
            node, l, h = visit.popleft()
            if node.val <= l or node.val >= h:
                return False
            if node.left:
                visit.append((node.left, l, node.val))
            if node.right:
                visit.append((node.right, node.val, h))
        return True

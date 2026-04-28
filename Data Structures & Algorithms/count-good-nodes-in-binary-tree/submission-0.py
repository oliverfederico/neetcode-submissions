# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # root node is always good
    # dfs so stack with node pointer and max val in path so far
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        visit = [(root, root.val-1)]
        while visit:
            node, mpv = visit.pop()
            if node.val >= mpv:
                mpv = node.val
                result+=1
            if node.right:
                visit.append((node.right, mpv))
            if node.left:
                visit.append((node.left, mpv))
        return result
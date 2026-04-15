# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]
        while queue:
            lh, rh = queue.pop()
            if lh and rh:
                if lh.val != rh.val:
                    return False
                queue.append((lh.left, rh.left))
                queue.append((lh.right, rh.right))
            elif not lh and not rh:
                continue
            else:
                return False
        return True

            
            
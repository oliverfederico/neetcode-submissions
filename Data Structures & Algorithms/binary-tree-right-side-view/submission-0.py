# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # return the rightmost node for each level of the tree, so we need to do top down bfs
    # add last node of each level to list
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        lq = deque()
        lq.append(root)
        while lq:
            q_len = len(lq)
            val = None
            for _ in range(q_len):
                node = lq.popleft()
                if node:
                    val = node.val
                    lq.append(node.left)
                    lq.append(node.right)
            if val:
                result.append(val)
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # breadth first search
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        node_queue = deque()
        if root:
            node_queue.append(root)
            node_queue.append(None)
        level_lst = []
        while node_queue:
            node = node_queue.popleft()
            if not node:
                result.append(level_lst)
                level_lst = []
                if node_queue and node_queue[0]:
                    node_queue.append(None)
            else:
                level_lst.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
        return result
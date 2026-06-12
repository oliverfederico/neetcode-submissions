# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                output.append(chr(0xFFFF))
                continue
            elif node.val <=0:
                output.append(chr(0xF000 | -node.val))
            else:
                output.append(chr(node.val))
            q.append(node.left)
            q.append(node.right)
        return ''.join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        head = TreeNode()
        curr = head
        level = deque()
        below = deque()
        for c in data:
            popped = False
            if not curr:
                curr = level.popleft()
                popped = True
            c_ord = ord(c)
            curr.left = curr.right
            if c_ord == 0xFFFF:
                curr.right = None    
            elif c_ord & 0xF000:
                curr.right = TreeNode(c_ord ^ 0xF000)
            else:
                curr.right = TreeNode(c_ord)
            if curr.right:
                below.append(curr.right)
            if not popped:
                curr = None
                if not level:
                    level, below = below, level
            # print(curr)
            # print(level)
            # print(below)
        return head.right

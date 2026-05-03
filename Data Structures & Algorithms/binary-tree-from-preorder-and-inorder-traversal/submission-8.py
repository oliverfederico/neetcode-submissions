# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
            
        root = TreeNode(preorder[0])
        curr = root
        j = 0
        
        for val in preorder[1:]:
            # If we haven't reached the current inorder node, keep building left
            if curr.val != inorder[j]:
                # Create left child and temporarily thread its right pointer back up to 'curr'
                curr.left = TreeNode(val, right=curr)
                curr = curr.left
            else:
                # We hit the bottom left. Advance inorder pointer.
                j += 1
                
                # Travel back UP the tree using our temporary right threads
                # Stop when we are about to hit a node that doesn't match the inorder sequence
                while curr.right and curr.right.val == inorder[j]:
                    temp = curr.right
                    curr.right = None  # Sever the temporary thread
                    curr = temp
                    j += 1
                
                # We've found the correct parent to attach the right child
                # The new right child inherits the parent's thread going up
                new_node = TreeNode(val, right=curr.right)
                curr.right = new_node
                curr = new_node
                
        # Final cleanup: If the tree is heavily left-skewed, we might finish 
        # the preorder traversal but still have lingering threads to sever.
        while curr and j < len(inorder) and curr.val == inorder[j]:
            temp = curr.right
            curr.right = None
            curr = temp
            j += 1
            
        return root
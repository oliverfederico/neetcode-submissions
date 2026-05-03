# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # preorder: node, left sub, right sub
    # inorder: left sub, node, right sub
    # while preorder !- inorder: we move left by increasing preorder
    # once preorder == inorder:
    # if inorder+1 != preorder.right 

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[0])
        node.right = node
        j = 0
        for x in preorder[1:]:
            # if we aren't at the node inorder yet
            if node.val != inorder[j]:
                # consume left sub
                node.left = TreeNode(x, right=node) 
                node = node.left
            else:
                # we are at the node
                j+=1
                #can't go right so we go up
                while node.right.val == inorder[j]:
                    temp = node.right
                    node.right = None
                    node = temp
                    j+=1
                # we can go right
                node.right = TreeNode(x, right=node.right)
                node = node.right
        while j < len(preorder) and node.val == inorder[j]:
            temp = node.right
            node.right = None
            node = temp
            j+=1
        return node
                    


                    
                    

            

            

            
            

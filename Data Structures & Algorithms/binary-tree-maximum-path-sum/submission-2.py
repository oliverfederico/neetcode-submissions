class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Base case for empty tree
        if not root:
            return 0
            
        global_max = float('-inf')

        def get_max_gain(node):
            nonlocal global_max
            if not node:
                return 0

            # Get max gain from left/right subtrees. 
            # We use max(..., 0) to instantly prune negative branches.
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            # The price to start a new path where `node` is the highest peak
            current_bridge_sum = node.val + left_gain + right_gain

            # Update global max if this new bridge is better
            global_max = max(global_max, current_bridge_sum)

            # Return the max gain if we continue ascending the current branch
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return global_max
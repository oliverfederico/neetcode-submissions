"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node.val == -1:
            clone = node.neighbors.pop()
            node.val = clone.val
            for neighbor in node.neighbors:
                if neighbor.val == -1:
                    self.cloneGraph(neighbor)
            return None
        else:
            clone = Node(node.val)
            node.val = -1
            node.neighbors.append(clone)

            for neighbor in node.neighbors[:-1]:
                if neighbor.val != -1:
                    cloned_neighbor = self.cloneGraph(neighbor)
                    if cloned_neighbor:
                        clone.neighbors.append(cloned_neighbor)
                else:
                    clone.neighbors.append(neighbor.neighbors[-1])   

            if clone.val == 1:
                self.cloneGraph(node)         
        return clone

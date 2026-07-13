"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        maps  = dict()
        def dfs(node):
            if node!=None:
                if node in maps:
                    return maps[node]
                clone = Node(node.val)
                maps[node]=clone
                for n in node.neighbors:
                    clone.neighbors.append(dfs(n))
            
                return clone
            else:
                return None
        print(node)
        return dfs(node)




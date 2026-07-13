# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        node = root
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node!=None:
                    temp = node.left
                    node.left = node.right
                    node.right=temp
                    q.append(node.left)
                    q.append(node.right)

        return root      

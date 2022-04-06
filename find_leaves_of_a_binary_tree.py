# Definition for a binary tree node.
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = defaultdict(list)
        
        
        def explore(node):
            if node:
                if node.left == None and node.right == None:
                    leaves[0].append(node.val)
                    return 0
            else:
                return 0
            
            left = explore(node.left)
            right = explore(node.right)
            height = 1 + max(left, right)
            leaves[height].append(node.val)
            return height
        
        explore(root)
        return leaves.values()
        
		
# OR


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = defaultdict(list)
        
        
        def explore(node, height):
            if not node:
                return height
            
            left = explore(node.left, height)
            right = explore(node.right, height)
            height = max(left, right)
            leaves[height].append(node.val)
            return 1 + height
        
        explore(root, 0)
        return leaves.values()
        
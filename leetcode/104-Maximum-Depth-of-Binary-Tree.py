# Difficulty : Easy
# Tag : Tree, DFS, BFS, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    maxLeft = self.maxDepth(root.left)+1
    maxRight = self.maxDepth(root.right)+1
    return max(maxLeft,maxRight)
    
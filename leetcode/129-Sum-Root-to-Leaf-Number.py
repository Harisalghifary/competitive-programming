# Difficulty : Medium
# Tag : Tree, DFS, BFS, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def traverseRootLeaf(currRoot, current):
        current *= 10
        current += currRoot.val
        
        if not currRoot.left and not currRoot.right:
            self.totalSum += current
            return 

        if currRoot.left:
            tLeft = traverseRootLeaf(currRoot.left, current)
            
        if currRoot.right:
            tRight = traverseRootLeaf(currRoot.right, current)

        return

    if not root.left and not root.right:
        return root.val
    self.totalSum = 0
    traverseRootLeaf(root,0)
    return self.totalSum
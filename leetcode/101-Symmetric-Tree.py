# Difficulty : Easy
# Tag : Tree, DFS, BFS, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isMirror(left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        if left.val != right.val:
            return False
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    if not root:
        return True
    else:
        return isMirror(root.left, root.right)
# Difficulty : easy
# Tag : Tree, DFS, BFS, BST, Binary Tree, Daily Leetcode CHallenge 15 June 2023
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    stack = []
    prev = minimum = 10**5+1
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
            
        root = stack.pop()
        minimum = min(minimum, abs(root.val-prev))
        prev = root.val
        root = root.right

    return minimum
            
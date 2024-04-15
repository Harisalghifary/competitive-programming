# Difficulty : Medium
# Tag : Binary Tree, Recursive, DFS
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node, path):
        nonlocal ans
        if not node:
            return
        if not node.left and not node.right:
            ans+= path*10 + node.val
        
        dfs(node.left, path*10 + node.val)
        dfs(node.right, path*10+ node.val)
    ans = 0
    dfs(root, 0)
    return ans
# Difficulty : Easy
# Tag : Binary Tree, recursive, queue
def minDepth(self, root: TreeNode) -> int:
        def solve(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if not root.left:
                return solve(root.right) +1
            if not root.right:
                return solve(root.left) +1

            left = solve(root.left)
            right = solve(root.right)

            return min(left,right)+1
        
        return solve(root)

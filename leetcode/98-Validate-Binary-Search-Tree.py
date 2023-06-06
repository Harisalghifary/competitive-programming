# Difficulty : Medium to Hard
# Tag : Tree, DFS, BFS, Binary Tree
def isValidBST(self, root: Optional[TreeNode]) -> bool: 
    # Define stack for store the node
    stack = []
    # prev for checking the previous node
    prev = None
    # check until root and stack is None
    # Inorder Traversal : left->root->right
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if prev and prev.val >= root.val:
            return False

        prev = root
        root = root.right

    return True
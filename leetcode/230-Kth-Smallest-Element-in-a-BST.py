# Difficulty : Medium
# Tag : Tree, DFS, BFS, Binary Tree, Priority Queue
# Time Complexity : O(n)
# Space Complexity : O(n) -> need to traverse until k node
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # Define variable
    stack = []
    index = 1
    # traverse condition
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        # check for kth smallest element
        if index == k:
            return root.val
        index +=1 
        root = root.right

    return 0
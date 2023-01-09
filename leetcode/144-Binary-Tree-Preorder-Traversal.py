# Easy Difficulty
# Tag : Stack, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#         if root:
#             result.append(root.val)
#             result = result + self.preorderTraversal(root.left)
#             result = result + self.preorderTraversal(root.right)
#         return result

# iteratively
    if root is None:
        return []
    current = root
    stack, result = [], []
    stack.append(current)

    while len(stack)>0:
        node = stack.pop()
        result.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return result
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_traversal(node):
    if node is None:
        return
    
    # Visit the current node
    print(node.value)
    
    # Traverse the left subtree
    depth_first_traversal(node.left)
    
    # Traverse the right subtree
    depth_first_traversal(node.right)

# Example binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Depth-First Traversal:")
depth_first_traversal(root)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_traversal_iterative(node):
    if node is None:
        return []
    
    result = []
    stack = [node]
    
    while stack:
        current = stack.pop()
        result.append(current.value)
        
        if current.right:
            stack.append(current.right)
        
        if current.left:
            stack.append(current.left)
    
    return result

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

print("Depth-First Traversal (Iterative):")
result = depth_first_traversal_iterative(root)
print(result)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(root):
    if root is None:
        return None

    min_value = float('inf')
    stack = [root]

    while stack:
        node = stack.pop()
        min_value = min(min_value, node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return min_value

# Example usage:
# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

# Find the minimum value in the binary tree using a stack
min_value = find_min_value(root)
print("Minimum value:", min_value)

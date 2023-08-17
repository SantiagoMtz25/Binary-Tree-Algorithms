class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(root):
    if root is None:
        return float('inf')  # Return positive infinity if tree is empty

    left_min = find_min_value(root.left)
    right_min = find_min_value(root.right)

    return min(root.value, left_min, right_min)

# Example usage:
# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

# Find the minimum value in the binary tree
min_value = find_min_value(root)
print("Minimum value:", min_value)

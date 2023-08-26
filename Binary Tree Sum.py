class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_binary_tree(root):
    if not root:
        return 0
    
    stack = [root]
    total_sum = 0
    
    while stack:
        current_node = stack.pop()
        total_sum += current_node.value
        
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    
    return total_sum

# Example usage:
# Construct a binary tree:    1
#                           /   \
#                          2     3
#                         / \   / \
#                        4   5 6   7
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

result = sum_binary_tree(tree)
print("Sum of binary tree values:", result)  # Output should be 28

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_in_binary_tree(root, target):
    if root is None:
        return False
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        if current.value == target:
            return True
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
    
    return False

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

target = 3
print(f"Searching for {target}: {search_in_binary_tree(root, target)}")

target = 6
print(f"Searching for {target}: {search_in_binary_tree(root, target)}")

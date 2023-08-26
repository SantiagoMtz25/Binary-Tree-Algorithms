class node :
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
  
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    sumBranch(root, 0, sums)
    return sums

def sumBranch(node, sum, sums):
    if node is None: 
        return

    newSum = sum + node.value
    if node.left is None and node.right is None:
        sums.append(newSum)
        return

    sumBranch(node.left, newSum, sums)
    sumBranch(node.right, newSum, sums)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    if not isinstance(root,TreeNode):
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)

    elif val < root.val:
        root.left = insert(root.left, val)
    return root


lst = [3,9,20,0,0,15,7]
root = None
for i in lst:
    root = insert(root, i)

def maxDepth(root) -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1



print(maxDepth(root))
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


lst = [10,6,15,4,8,12,20,1,5,9,11,13,19,21]
root = None
for i in lst:
    root = insert(root, i)

def invertTree(root):
    if not isinstance(root, TreeNode):
        return None
    if root.left and root.right:
        root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root



invertTree(root)
print('hh')
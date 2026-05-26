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


def invertTree(root):
    if not isinstance(root, TreeNode):
        return None
    if root.left and root.right:
        root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

lst = [5,3,6,2,4,0,0,1]
k = 3
root = None
for i in lst:
    root = insert(root, i)

def kthSmallest(root, k: int) -> int:
    def inorder(root):
        if not isinstance(root, TreeNode):
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)
    return inorder(root)[k-1]

print(kthSmallest(root,2))


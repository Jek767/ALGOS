from sys import pycache_prefix


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root: Node, val):
    if not isinstance(root,Node):
        return Node(val)

    if val > root.val:
        root.right = insert(root.right, val)

    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def preorder(root):
    if not isinstance(root,Node):
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

lst = [10,5,15,3,7,20]
root = None
for i in lst:
    root = insert(root, i)

print(preorder(root))
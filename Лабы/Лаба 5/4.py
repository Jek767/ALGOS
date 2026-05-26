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

lst = [5,4,6,0,0,3,7]
root = None
for i in lst:
    root = insert(root, i)


def isValidBST(root) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))


print(isValidBST(root))


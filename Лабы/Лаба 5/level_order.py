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

def level_order(root):
    if not isinstance(root,Node):
        return []
    result = []
    root_list = [root]
    while root_list:
        level = []
        for i in range(len(root_list)):
            node = root_list.pop(0)
            level.append(node.val)
            if node.left:
                root_list.append(node.left)
            if node.right:
                root_list.append(node.right)
        result.append(level)
    return result

lst = [10,5,15,3,7,20]
root = None
for i in lst:
    root = insert(root, i)

print(level_order(root))
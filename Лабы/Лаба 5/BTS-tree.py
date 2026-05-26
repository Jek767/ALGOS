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

def search(root: Node, val):
    if not isinstance(root,Node):
        print("Элемент отсутствует в дереве")
        return
    if root.val == val:
        return root
    elif val > root.val:
        root.right = search(root.right, val)
    elif val < root.val:
        root.left = search(root.left, val)

def find_min(root):
    mini = root
    while mini.left:
        mini = mini.left
    return mini

def delete(root: Node, val):
    if not isinstance(root,Node):
        print("Элемент отсутствует в дереве")
        return

    if root.val == val:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp = find_min(root.right)
        root.val = temp.val
        delete(root.right, temp.val)

    elif val > root.val:
        root.right = delete(root.right, val)

    elif val < root.val:
        root.left = delete(root.left, val)

root = Node(11)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 12)
root = insert(root, 15)

test = search(root,10)
print(test)





class Node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    
    else:
        if key <root.data:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    print(left_height,right_height)
    return max(left_height ,right_height) + 1

def search(root, key):
    if root is None or root.data == key:
        return root.data
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)





root = None
lst = [7,8,9,1,5,6,2]
for i in lst:
    root = insert(root,i)


inorder_traversal(root)
# print()
# preorder(root)
# print()
# postorder_traversal(root)
print('\n',height(root))
print(search(root,2))
        
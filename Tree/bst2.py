class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    
    if key< root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height,right_height)+1
    

def search(root,key):
    if root is None:
        return 0
    if root.data == key:
        root.data = 0
    if key < root.data:
        return search(root.left,key)
    return search(root.right,key)

def delete1(key):
    delete(root,key)

def delete(root,key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current



root = None
lst = [5,1,2,3,4,6,7,8,9]
for i in lst:
    root = insert(root,i)


# inorder(root)
# preorder(root)
# postorder(root)
# print(height(root))
# search(root,7)
# postorder(root)
delete1(6)
inorder(root)


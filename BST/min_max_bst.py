class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# Example usage
def fin_min(root):
    current=root
    while current.left:       
        current=current.left
    return current.key
def find_max(root):
    current=root
    while current.right:       
        current=current.right
    return current.key
  

root=None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("Inorder traversal:")
# fin_min(root)
print("Minimum value in BST:", fin_min(root))
print("Minimum value in BST:", find_max(root))

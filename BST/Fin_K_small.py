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
count = [0]  # Mutable counter
result = [None]
def fin_min(root):
   



  

root=None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("Inorder traversal:")
# fin_min(root)
print("Minimum value in BST:", fin_min(root))

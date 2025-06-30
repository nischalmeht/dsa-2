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

def tree_sum(root):
    # print(root.key)
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right) 
# print (root)

if __name__ == "__main__":
    root = None
    for val in [1, 2, 3]:
        root = insert(root, val)
    
    result = tree_sum(root)
    print("Sum of all nodes:", result)

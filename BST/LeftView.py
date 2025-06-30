class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def recLeftView(root, level, result):
    if root is None:
        return
    
    if level == len(result):
        result.append(root.data)
    
    recLeftView(root.left, level + 1, result)
    recLeftView(root.right, level + 1, result)

def leftView(root):
    result = []
    recLeftView(root, 0, result)
    return result

# Main function
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = leftView(root)
    print(result)
    # print(' '.join(map(str, result)))  # Output: 1 2 4
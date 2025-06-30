class Node:
    def __init__(self, data):
        self.data = data
        self.next = None     # Points to the next node in top-level list
        self.bottom = None   # Points to the next node in bottom (sub) list

def merge(a, b):
    if not a: return b
    if not b: return a

    if a.data < b.data:
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)

    result.next = None  
    return result

def flatten(root):
    if not root or not root.next:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root

def print_flattened_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.bottom
    print("None")

# Example usage
if __name__ == "__main__":
    # Construct the list manually
    # 5 -> 10 -> 19 -> 28
    # |     |     |     |
    # V     V     V     V
    # 7     20    22    35
    # |           |     |
    # V           V     V
    # 8           50    40
    # |                 |
    # V                 V
    # 30                45

    head = Node(5)
    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next = Node(10)
    head.next.bottom = Node(20)

    head.next.next = Node(19)
    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next = Node(28)
    head.next.next.next.bottom = Node(35)
    head.next.next.next.bottom.bottom = Node(40)
    head.next.next.next.bottom.bottom.bottom = Node(45)

    flat_head = flatten(head)
    print_flattened_list(flat_head)

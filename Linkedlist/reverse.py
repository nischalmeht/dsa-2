class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Print original list
current = node1
print("Original list:")
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")

# Reverse the linked list
prev = None
current = node1  # Reset current to head
while current:
    nxt = current.next
    current.next = prev
    prev = current
    current = nxt

# Print reversed list
print("Reversed list:")
current = prev
while current:
    print(current.data, end="->")
    current = current.next
print("None")

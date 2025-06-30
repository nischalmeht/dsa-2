class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse(head):
    current = head
    temp = None

    while current is not None:
        # Swap prev and next
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp is not None:
        head = temp.prev

    return head

def print_list(head):
    while head:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

# Create the doubly linked list: 1 <-> 2 <-> 3 <-> 4
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

# Reverse and print
head = reverse(head)
print("Reversed list:")
print_list(head)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse(head):
    prev=None
    current=head
    while current is not None:
        next=current.next
        current.next=prev
        prev=current
        current=next
    return prev
def delete_nodes_with_greater_right(head):
    head= reverse(head)
    max_node=head
    current=head
    while current.next is not None:
        if current.next.data < max_node.data:
            current.next=current.next.next
        else:
            current=current.next
            max_node=current
    head=reverse(head)
    return head
def print_list(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("None")

# Example usage
node1 = Node(12)
node2 = Node(15)
node3 = Node(10)
node4 = Node(11)
node5 = Node(5)
node6 = Node(6)
node7 = Node(2)
node8 = Node(3)

# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

# Process the list
new_head = delete_nodes_with_greater_right(node1)
print_list(new_head)

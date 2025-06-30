class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_loop_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    #     if slow == fast:
    #         break
    # else:
    #     return None  
    # slow = head
    # while slow != fast:
    #     slow = slow.next
    #     fast = fast.next

    # return slow  

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

head=Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node3  

start_node = find_loop_start(head)
print(start_node)
if start_node:
    print("Loop starts at node with data:", start_node.data)
else:
    print("No loop detected.")

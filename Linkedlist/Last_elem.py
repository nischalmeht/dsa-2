class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node2=Node(20)
node3=Node(20)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4

current=node1

while current.next is not None:
    if current.data == current.next.data:
        current.next=current.next.next
    else:
        current=current.next

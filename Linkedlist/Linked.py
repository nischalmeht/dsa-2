class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None

    def reverse(self):
        temp=self.head
        prev=None
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next

if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insert_end(10)
    sll.insert_end(20)
    sll.insert_end(30)
    sll.insert_end(40)
    sll.insert_beg(50)
    # sll.reverse()
    print("Singly Linked List:")
    # sll.display()        
    sll.middle()
    sll.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Fixed this line

def remove_duplicate(head):
    if head is None:  # Fixed logic
        return head

    seen = set()
    current = head
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage:
head = Node(10)
head.next = Node(20)
head.next.next = Node(10)
head.next.next.next = Node(30)

print("Original list:")
print_list(head)

head = remove_duplicate(head)

print("List after removing duplicates:")
print_list(head)

def inorder (root):
    stack=[]
    curr=root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
    curr=stack.pop()
    print(curr.data)
    curr=curr.right

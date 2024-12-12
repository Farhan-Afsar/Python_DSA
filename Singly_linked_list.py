class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)

Head.next = a
a.next = b
b.next = c

#Traversal - O(n)
curr = Head

while curr:
    print(curr)
    curr = curr.next

#display - O(n)

def display(Head):
    curr = Head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    
    print(' -> '.join(element))

display(Head)

#Search - O(n)

def search(Head,val):
    curr = Head
    pos = 1
    while curr:
        if curr.val == val:
            print(pos)
            return True
        curr = curr.next
        pos+=1
    return False

print(search(Head,4))
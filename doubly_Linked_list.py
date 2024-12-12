class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

head = tail = Node(1)



#display - O(n)

def display(Head):
    curr = Head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    
    print(' <-> '.join(element))

display(head)

#insert_head - O(1)
def insert_head(head,tail,val):
    new = Node(val,next = head)
    head.prev = new
    return new,tail

head,tail = insert_head(head,tail,3)
display(head)

#insert_tail - O(1)
def insert_tail(head,tail,val):
    new = Node(val,prev = tail)
    tail.next = new
    return head,new

head,tail = insert_tail(head,tail,7)
display(head)

#Traversal - O(n)
curr = head

while curr:
    print(curr)
    curr = curr.next

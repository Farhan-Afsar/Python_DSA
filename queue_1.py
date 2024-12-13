from collections import deque
q = deque()
print(q)

#Enqueue - O(1)
q.append(1)
q.append(2)
q.append(3)

print(q)

#Dequeue - O(1)

q.popleft()
print(q)

#Lookup - O(1)

print(q[0])
print(q[-1])
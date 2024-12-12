a = [1,2,3,4]
print(a)

#Append - Insert element at end - on average O(1)
a.append(5)
print(a)

#Pop - delete element at end - on average O(1)
a.pop()
print(a)

#insert - not at end - O(n)
a.insert(1,0)
print(a)

#Modify an element - O(1)
a[0] = 9
print(a)

#Access an element - O(1)
print(a[0])

#Check if array has an element - O(n)

if 9 in a:
    print(True)


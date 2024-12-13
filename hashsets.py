s = set()
print(s)

# add - O(n)

s.add(1)
s.add(2)
s.add(3)
print(s)

#Search - O(1)

if 2 in s:
    print(True)

#remove - O(1)
s.remove(3)
print(s)

#print

for x in s:
    print(x)

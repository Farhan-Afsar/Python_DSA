#Append end of the string - O(n)

a = "Hello"
b = a + 'b'
print(b)

#Check something in the string - O(n)

if 'f' in b:
    print(True)

#Access - O(1)
print(b[0])

#Length - O(1)
print(len(b))
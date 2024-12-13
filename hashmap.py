#Dictionary

d = {
    'Farhan':1,
    'Afsar': 2,
    'Hi': 3
}

print(d)

#Add - O(1)

d['Hlw'] = 4
print(d)

#Check Key - O(1)

if 'Farhan' in d:
    print(True)

#Check value of any key - O(1)

print(d['Farhan'])

#Loop -O(n)

for key,val in d.items():
    print(f'Key:{key},value: {val}')

#Default Dict 

from collections import defaultdict
default = defaultdict(list)
print(default[2])

#Counter

from collections import Counter

counter = Counter("Farhan Afsar")
print(counter)
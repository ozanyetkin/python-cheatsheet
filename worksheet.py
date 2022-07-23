a = 'end'
b = {'end', 'a', 'b', 'C'}
c = set()

c.difference(b)
b.remove('b')
print(b)
print(b.difference(set(a)))
print(list(filter(lambda x: x.islower(), b)))

c = []

for i in c:
    pass
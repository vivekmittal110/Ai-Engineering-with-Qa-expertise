l = []
l.append(3)
l.append(2)
l.append(3)
l.append(4)

del l[0]
del l[0]
del l[0]
del l[0]

# print(l[0])
print(l)
print(None) if l == [] else print(len(l))
# [8,1,2,2,3]
a = [8,1,2,2,3]
c = sorted(a)
print(sorted(a))
new = []
for i in a:
    count = 0
    for j in c:
        if i == j:
            break
        if i>j:
            count+=1
    new.append(count)
print(new)
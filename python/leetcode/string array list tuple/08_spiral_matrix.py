'''
 c 0 1 2 3 4
r0 1 2 3 4 6
r1 5 6 7 8 6
r2 9 8 6 4 8
r3 3 3 6 8 4
'''
matrix = [[1,2,3],[4,5,6],[7,8,9],[2,3,4]]
n = len(matrix)
m = len(matrix[0])
ans = []
total = m*n
r_start = 0
r_end = n-1
c_start = 0
c_end = m-1
c = 0
while total>c:
    for i in range(c_start,c_end+1):
        ans.append(matrix[r_start][i])
        c+=1
    r_start+=1
    if total == c:
        break
    for i in range(r_start,r_end+1):
        ans.append(matrix[i][c_end])
        c+=1
    c_end-=1
    if total ==c:
        break
    for i in range (c_end,c_start-1,-1):
        ans.append(matrix[r_end][i])
        c+=1
    r_end-=1
    if total==c:
        break
    for i in range (r_end,r_start-1,-1):
        ans.append(matrix[i][c_start])
        c+=1
    c_start+=1
    if total == c:
        break

print(ans)

accounts = [[1,5],[7,3],[3,5]]
curr_rich = 0
for i in accounts:
    if curr_rich<sum(i):
        curr_rich=sum(i)
print(curr_rich)
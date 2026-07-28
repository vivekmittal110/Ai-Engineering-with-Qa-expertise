candies = [2,3,4,2,1]
extraCandies = 2
grt = max(candies)
out = []
for i in candies:
    if i+extraCandies >= grt:
        out.append(True)
    else:
        out.append(False)
print(out)
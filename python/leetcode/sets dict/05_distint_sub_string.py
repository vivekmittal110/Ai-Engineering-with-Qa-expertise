s = "aababcabc"
n = len(s)-2
ans=0
for i in range(0,n):
    if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
        ans +=1
print(ans)
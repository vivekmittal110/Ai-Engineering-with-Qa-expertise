s = "abcabcbb"
ans = 1
for i in range(s):
    curr = s[i]
    if s[i] == curr:
        ans = 1
    else:
        ans+=1
s = "aa"
t = "a"
dict1 = {}
dict2 = {}
        
for i in range (0,len(s)):
    if s[i] in dict1:
        dict1[s[i]]+=1
    else:
        dict1[s[i]]=0
for i in range (0,len(t)):
    if t[i] in dict2:
        dict2[t[i]]+=1
    else:
        dict2[t[i]]=0
print(dict1)
print(dict2)
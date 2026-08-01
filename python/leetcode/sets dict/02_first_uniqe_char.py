s = "loveleetcode"
n = len(s)
dict1={}
ret = -1
for i in range(0,n):
    if s[i] in dict1:
        dict1[s[i]]+=1
    else:
        dict1[s[i]]=0
for key,value in dict1.items():
    if value == 0:
        ret=key
        print(s.index(ret))
        break
print(ret)
print(dict1)
def ssort(s):
    s = list(s)
    s.sort()
    return "".join(s)
strs = ["eat","tea","tan","ate","nat","bat"]
dict1={}
lst=[]
for i in strs:
    key = ssort(i)
    if key in dict1:
        dict1[key]+=[i]
    else:
        dict1[key]=[i]
    # print(key)
for key,value in dict1.items():
    lst += [value]
# print(dict1)
print(lst)
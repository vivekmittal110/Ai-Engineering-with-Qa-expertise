s = "A man, a plan, a canal: Panama"
st = s.lower()
new=""
for i in st:
    if i in "abcdefghijklmnopqrstuvwxyz":
        new+=i
rev = new[::-1]
print(new==rev)

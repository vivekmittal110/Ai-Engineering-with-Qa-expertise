
# f = open("poem.txt")
with open("poem.txt","w") as w:
    st = "twinkle twinkle little star"
    w.write(st)
with open("poem.txt") as f:
    data = f.read()
    if "twinkle" in data:
        print("yes")
    else:
        print("no")
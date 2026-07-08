def rem(l,word):
    n = []
    for i in l:
        if i != word:
            n.append(i.strip(word))
    return n



l = ["vivek", "sachin", "rohit", "virat", "dhoni","ekta"]
print(rem(l,"ek"))
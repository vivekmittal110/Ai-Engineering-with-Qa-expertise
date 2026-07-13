words = ["donkey","bad","yo"]
with open("donkey.txt","r") as f:
    content = f.read()
for i in words:
    content = content.replace(i,"####")

with open("donkey.txt","w") as w:
    w.write(content)

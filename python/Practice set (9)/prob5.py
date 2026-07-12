word = "####"
with open("donkey.txt","r") as f:
    content = f.read()

new_content = content.replace(word,"donkey")

with open("donkey.txt","w") as w:
    w.write(new_content)

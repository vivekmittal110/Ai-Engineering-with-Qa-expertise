with open("donkey.txt") as f:
    line = f.readline()
    line_number = 0
    found = 0
    while line != "":
        line_number += 1
        if "python" in line:
            found = line_number
            break
        line = f.readline()
if found == 0:
    print("Not found")
else:
    print(f"Found in line {found}")
try:   
    with open("sample.txt", "r+") as file:
        file.write("Hello vivek \n")
        file.writelines(["gayatri\n", "vivek ", "divyam"])
        file.seek(0)
        contant = file.readlines()
        print(contant)
except FileNotFoundError:
    print("File not found")
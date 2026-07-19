try:
    with (open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3):
        print("Files opened successfully")
except FileNotFoundError:
    print("File not found")
for i in range(2,21):
    with open(f"table/table_of_{i}.txt","a") as w:
        for k in range (1,11):
            w.write(f"{i} X {k} = {i*k}\n")
        
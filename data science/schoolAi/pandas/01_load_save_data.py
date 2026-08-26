import pandas as pd

df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

df.to_excel("data.xlsx")
df.to_csv("data.csv")
df.to_csv("data.csv", index=False)
print(df)
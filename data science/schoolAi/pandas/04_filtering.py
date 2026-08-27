import pandas as pd


data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df = pd.DataFrame(data)

selected = df[["species","sepal_length"]]
print(selected)


filtered = df[(df["sepal_length"]>5.0) & (df["species"]=='setosa')]
print(filtered)
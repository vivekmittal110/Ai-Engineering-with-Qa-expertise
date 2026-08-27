import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df = pd.DataFrame(data)
print(df.head(5))
print(df.tail(5))
# print(df.info())
print(df.describe())
# print(df)
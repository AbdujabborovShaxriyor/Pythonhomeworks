import pandas as pd

#task1
df = pd.read_json("iris.json")
df.columns = df.columns.str.lower()
df = df[["sepal_length","sepal_width"]]

#task2
df = pd.read_excel("titanic.xlsx")
df_filtered = df[df["age"]>30]
print(df_filtered["gender"].value_counts())

#task3
df = pd.read_parquet("flights.parquet")
print(df["origin"])
print(df["dest"])
print(df["carrier"])
df_unique = df.drop_duplicates()
print(df_unique['dest'].value_counts())

#task4
df =  pd.read_csv("movie.csv")
df_filtered = df[df['duration ']>120]
df_filtered.sort_values(by='director_facebook_likes',ascending=False)
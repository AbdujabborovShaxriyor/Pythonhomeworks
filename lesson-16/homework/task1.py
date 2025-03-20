import pandas as pd
import sqlite3

#task1
connection=sqlite3.connect("chinook.db")
df = pd.read_sql("SELECT * FROM customers",con=connection)
print(df.head(10))

#task2
df = pd.read_json("iris.json")
print(df.shape)
print(df.columns)

#task3
df = pd.read_excel("titanic.xlsx")
print(df.head())

#task4
df = pd.read_parquet("flights.parquet")
print(df.info())

#task5
df =  pd.read_csv("movie.csv")
print(df.sample(10))
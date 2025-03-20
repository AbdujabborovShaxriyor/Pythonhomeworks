import pandas as pd

#task1
df = pd.read_json("iris.json")
mean_values = df.mean(numeric_only=True)
median_values = df.median(numeric_only=True)
std = df.std(numeric_only=True)

#task2
df = pd.read_excel("titanic.xlsx")
maximum_val = df.max(numeric_only=True)
minimum_val = df.min(numeric_only=True)
sum_val = df.sum(numeric_only=True)

#task3
df =  pd.read_csv("movie.csv")
most_liked_director = df[df['director_facebook_likes'] == df['director_facebook_likes'].max()]['director']
longest_movies = df[['movie_title', 'director_name', 'duration']].sort_values(by='duration', ascending=False).head(5)

#task4
df = pd.read_parquet("flights.parquet")
filled_df = df.fillna(df.mean(numeric_only=True),inplace=True)
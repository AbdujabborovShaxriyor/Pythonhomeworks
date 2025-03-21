import pandas as pd
import sqlite3
from sklearn.preprocessing import MinMaxScaler

#task1
connection = sqlite3.connect("chinook.db")
df1 = pd.read_sql('SELECT * FROM customers',con=connection)
df2 = pd.read_sql('SELECT * FROM invoices',con=connection)
df3 = pd.merge(df1,df2,on='CustomerId',how='inner')
count_invoice = df3.groupby('CustomerID')['invoiceID'].count()

#task2
df = pd.read_csv('movie.csv')
df1 = df[['director_name','color']]
df2 = df[['director_name','num_critic_for_reviews']]
df3 = pd.merge(df1,df2,on='director_name',how='left')
df4 = pd.merge(df1,df2,on='director_name',how='outer')
pd.options.display.max_rows=999999999999
count_left = df3['director_name'].count()
count_outer = df4['director_name'].count()

#task3
df = pd.read_csv('titanic.csv')
avg_age = df.groupby('Pclass')['Age'].mean()
total_fare = df.groupby('Pclass')['Fare'].sum()
passengers = df.groupby('Pclass')['Passengers'].sum()
data = {
    'Average_age':avg_age,
    'Total_fare':total_fare,
    'Passengers':passengers
}
new_df = pd.DataFrame(data)

#task4
df = pd.read_json('movie.json')
result = df.groupby(['color','director_name']).agg({
    'num_critic_for_reviews':'sum',
    'duration': 'mean'
}).reset_index()

#task5
df = pd.read_csv('flight.csv')
result = df.groupby(['Year','Month']).agg({
    'Total_flights':'sum',
    'ArrDelay':'mean',
    'DepDelay':'max'
})

#task6
def child_or_adult(age):
    if age<18:
        return 'Child'
    else:
        return 'Adult'
df = pd.read_csv('titanic.csv')
df['age_group'] = df['Age'].apply(child_or_adult)

#task7
def normalize(group):
    scaler = MinMaxScaler()
    group['Normalized_Salary'] = scaler.fit_transform(group[['Salary']])
    return group
df = pd.read_csv('employee.csv')
result = df.groupby('Department').apply(normalize)

#task8
df = pd.read_csv('movie.csv')
def categorize(duration):
    if duration<60:
        return 'Short'
    elif duration<120 and duration>60:
        return 'Medium'
    else:
        return 'Long'
df['Category'] = df['duration'].apply(categorize)

#task9
df = pd.read_csv('titanic.csv')
def filter_alive(df):
    return df[df['survived']==1]
    
def fill_age(df):
    df['age'].fillna(df['age'].mean(),inplace=True)
    return df
def Fare_Per_Age(df):
    df['Fare_Per_Age'] = df['fare']/df['age']
    return df
df = (
    df.pipe(filter_alive)
    .pipe(fill_age)
    .pipe(Fare_Per_Age)
)

#task10
df = pd.read_csv('flights.csv')
def filter_flights(df):
    return df[df['Delay']>30]
def Delay_Per_Hour(df):
    if df['flight_duration']!=0:
        df['Delay_Per_Hour'] = df['Delay']/df['flight_duration']
        return df
    else:
        return 0
df=(
    df.pipe(filter_flights)
    .pipe(Delay_Per_Hour)
)
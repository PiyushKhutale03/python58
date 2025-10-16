import pandas as pd

#Series
data = [10, 20, 30, 40]
s = pd.Series(data)

data = [90, 85, 75]
labels = ['Math', 'Science', 'English']
marks = pd.Series(data, index=labels)

print(marks)

#Dataframe

print("\n")
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data1)
print(df)





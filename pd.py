import pandas as pd
#Series
a=[1,7,2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["x"])

calories={"day1":2400,"day2":3500,"day3":2600}
myvar1=pd.Series(calories)
print(myvar1)


#Dataframe

data = {"calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }

df = pd.DataFrame(data)

print(df) 
print(df.loc[[0,1]])


#csv
df=pd.read_csv('data.csv')
print(df)
print(pd.options.display.max_rows) 


#json
df = pd.read_json('data.json')

print(df.to_string()) 
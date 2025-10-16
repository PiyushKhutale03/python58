import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

# Step 2: Save DataFrame to a CSV file
df.to_csv('people.csv', index=False) 
print("CSV file 'people.csv' created.\n")

# Step 3: Read the CSV file
df_read = pd.read_csv('people.csv')

# Step 4: Print the contents
print("Contents of the CSV file:")
print(df_read)

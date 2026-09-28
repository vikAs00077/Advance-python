import pandas as pd

data = {
    "Name": ["Amit", "Ravi", "Neha", "Sara"],
    "Age": [21, 22, 20, 23],
    "Marks": [78, 85, 92, 66]
}

df = pd.DataFrame(data)
print(df)


import pandas as pd

data = {"Name": ["Amit", "Ravi", "Neha"], "Marks": [78, None, 92]}
df = pd.DataFrame(data)

print(df.isnull())        # Check missing values
print(df.dropna())        # Remove rows with missing values
print(df.fillna(0))       # Replace missing values with 0


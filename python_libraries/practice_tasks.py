import pandas as pd

# Create the DataFrame
data = {
    'Name': ['John', 'Mary', 'Peter'],
    'Age': [20, 22, 21],
    'Grade': [65, 48, 82]
}

df = pd.DataFrame(data)
print(df)

df['Passed'] = df['Grade'] > 50
print(df)

passed_students = df[df['Passed'] == True]
print(passed_students)



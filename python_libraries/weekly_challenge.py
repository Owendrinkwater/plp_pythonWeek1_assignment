import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

numbers = np.arange(1, 11)
mean_value = np.mean(numbers)

print("NumPy Array:", numbers)
print("Mean:", mean_value)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, 30, 22, 28],
    'Score': [85, 90, 95, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print("\nJoke Setup:", joke['setup'])
    print("Punchline:", joke['punchline'])
else:
    print("Failed to fetch data")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

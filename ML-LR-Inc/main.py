import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sea
import plotly.express as px # it is not working PC GUI but working on web browser

data = pd.read_csv('expenses.csv')

# print(data)

# print(data.info())

# print(data.describe())



plt.figure(figsize=(10, 6))
plt.hist(data['age'], bins=47, edgecolor='black', alpha=0.7)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()




import numpy as mp
import pandas as pd



df = pd.read_csv('house_prices.csv')
print(df)


# df = pd.read_csv('data.csv')
# missing_values = df.isnull().sum()
# print(missing_values)


# Remove Missing Values
df.dropna(inplace=True)



# Impute Missing Values:
df.fillna(df.mean(), inplace=True)  # For numerical columns
df['column_name'].fillna('default_value', inplace=True)  # For categorical columns



# Remove Duplicates
df.drop_duplicates(inplace=True)


# Normalization
df['normalized_column'] = (df['column_name'] - df['column_name'].min()) / (df['column_name'].max() - df['column_name'].min())


# Standardization
df['standardized_column'] = (df['column_name'] - df['column_name'].mean()) / df['column_name'].std()




# Convert Categorical Variables
# Use one-hot encoding or label encoding
df = pd.get_dummies(df, columns=['categorical_column'], drop_first=True)




# Feature Engineering
# Create new features from existing ones to improve model performance
df['new_feature'] = df['feature1'] * df['feature2']




df_grouped = df.groupby('category_column').agg({'value_column': ['mean', 'sum']})

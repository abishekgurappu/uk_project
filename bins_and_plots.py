import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('heart_disease.db')

def table_to_dataframe():
    query = "SELECT * FROM heart_disease_data"
    df = pd.read_sql_query(query, conn)
    return df

def bucket_continuous_values(df, column, bins):
    df[column + '_bucket'] = pd.cut(df[column], bins)
    return df

def generate_table_of_counts(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, 'Count']
    return counts


def plot_counts_bar(counts, column):
    plt.figure(figsize=(10, 6))
    plt.bar(counts[column].astype(str), counts['Count'], color='skyblue')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Counts for {column} Buckets')
    plt.xticks(rotation=45)
    plt.show()


df = table_to_dataframe()


continuous_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
bin_ranges = {'age': range(20, 100, 10),
              'trestbps': range(80, 210, 10),
              'chol': range(100, 600, 50),
              'thalach': range(70, 210, 10),
              'oldpeak': [0, 1, 2, 3, 4, 5]}


for column in continuous_columns:
    df = bucket_continuous_values(df, column, bin_ranges[column])
    counts = generate_table_of_counts(df, column + '_bucket')
    print(f"Counts for {column} Buckets:")
    print(counts)
    plot_counts_bar(counts, column + '_bucket')

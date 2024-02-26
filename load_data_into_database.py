import os
import sqlite3

conn = sqlite3.connect('heart_disease.db')

def create_table():
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS heart_disease_data (
        id INTEGER PRIMARY KEY,
        age INTEGER,
        sex INTEGER,
        cp INTEGER,
        trestbps INTEGER,
        chol INTEGER,
        fbs INTEGER,
        restecg INTEGER,
        thalach INTEGER,
        exang INTEGER,
        oldpeak REAL,
        slope INTEGER,
        ca INTEGER,
        thal INTEGER,
        num INTEGER
    )
    """
    conn.execute(create_table_sql)
    print("Successfully created table")

def insert_data(data):
    insert_sql = """
    INSERT INTO heart_disease_data (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, num)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    conn.executemany(insert_sql, data)


def read_dat_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            values = [None if value == '?' else int(value) if value.isdigit() else float(value) if '.' in value else value for value in values]
            data.append(values)
    return data

folder_path = 'heart_disease_data\processed' 

create_table()

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    data = read_dat_file(file_path)
    insert_data(data)

conn.commit()
conn.close()

print("Data from all files has been successfully inserted into the SQLite database.")

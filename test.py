import sqlite3

conn = sqlite3.connect('heart_disease.db')

def fetch_first_five_rows():
    query = "SELECT * FROM heart_disease_data LIMIT 5"
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    return rows


def count_rows():
    query = "SELECT COUNT(*) FROM heart_disease_data"
    cursor = conn.execute(query)
    count = cursor.fetchone()[0]
    return count


first_five_rows = fetch_first_five_rows()
print("First five rows:")
for row in first_five_rows:
    print(row)

total_rows = count_rows()
print("Total number of rows:", total_rows)
conn.close()


import sqlite3
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT,
    gender TEXT,
    payment TEXT,
    city TEXT,
    grade TEXT,
    age INTEGER,
    quantity INTEGER,
    total INTEGER
)
""")

df = pd.read_csv("customers.csv", encoding="utf-8")

print(df.columns.tolist())

data = list(
    df[['고객ID', '성별', '결제수단', '거주지', '회원등급', '나이', '구매수량', '총결제금액']]
    .itertuples(index=False, name=None)
)

cursor.executemany("""
INSERT INTO customers
(customer_id, gender, payment, city, grade, age, quantity, total)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", data)

conn.commit()

cursor.execute("SELECT * FROM customers LIMIT 5")
rows = cursor.fetchall()

print("\n데이터:")
for row in rows:
    print(row)

cursor.execute("UPDATE customers SET city=? WHERE customer_id=?", ("Seoul", "CUST_0001"))
conn.commit()

cursor.execute("DELETE FROM customers WHERE customer_id=?", ("CUST_0002",))
conn.commit()

conn.close()
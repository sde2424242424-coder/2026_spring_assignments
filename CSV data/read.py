def read_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers LIMIT 5")

    rows = cursor.fetchall()

    print("\n📊 데이터:")
    for row in rows:
        print(row)
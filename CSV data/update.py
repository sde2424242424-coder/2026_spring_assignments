def update_data(conn):
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE customers SET city=? WHERE customer_id=?",
        ("Seoul", "CUST_0001")
    )

    conn.commit()
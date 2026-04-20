def delete_data(conn):
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE customer_id=?",
        ("CUST_0002",)
    )

    conn.commit()
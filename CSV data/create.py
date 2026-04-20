import pandas as pd

URL = "https://raw.githubusercontent.com/ancestor9/data/main/customers.csv"

def insert_data(conn):
    df = pd.read_csv(URL)

    data = list(df[['고객ID', '성별', '결제수단', '거주지', '회원등급',
                    '만족도', '최근접속시간(시)', '선호제품군_적정온도',
                    '나이', '구매수량', '총결제금액']]
                .itertuples(index=False, name=None))

    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO customers
        (customer_id, gender, payment, city, grade,
         satisfaction, last_login, temperature,
         age, quantity, total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
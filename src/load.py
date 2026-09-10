from database import get_connection


def create_tables():

    conn = get_connection()

    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXISTS fact_sales (
                order_id INTEGER PRIMARY KEY,
                customer_id VARCHAR(20),
                customer_name VARCHAR(100),
                product VARCHAR(100),
                quantity INTEGER,
                unit_price NUMERIC(10,2),
                order_date DATE,
                status VARCHAR(20),
                total_amount NUMERIC(12,2)
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS rejected_sales (
                id SERIAL PRIMARY KEY,
                order_id INTEGER,
                customer_id VARCHAR(20),
                customer_name VARCHAR(100),
                product VARCHAR(100),
                quantity INTEGER,
                unit_price NUMERIC(10,2),
                order_date DATE,
                status VARCHAR(20),
                rejection_reason TEXT
            );
        """)

    conn.commit()
    conn.close()


def load_data(valid_records, rejected_records):

    conn = get_connection()

    with conn.cursor() as cur:

        # Clean previous run
        cur.execute("TRUNCATE TABLE fact_sales;")
        cur.execute("TRUNCATE TABLE rejected_sales RESTART IDENTITY;")

        for _, row in valid_records.iterrows():

            cur.execute("""
                INSERT INTO fact_sales
                (
                    order_id,
                    customer_id,
                    customer_name,
                    product,
                    quantity,
                    unit_price,
                    order_date,
                    status,
                    total_amount
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                int(row["order_id"]),
                row["customer_id"],
                row["customer_name"],
                row["product"],
                int(row["quantity"]),
                float(row["unit_price"]),
                row["order_date"],
                row["status"],
                float(row["total_amount"])
            ))

        for _, row in rejected_records.iterrows():

            unit_price = (
                None
                if row["unit_price"] != row["unit_price"]
                else float(row["unit_price"])
            )

            cur.execute("""
                INSERT INTO rejected_sales
                (
                    order_id,
                    customer_id,
                    customer_name,
                    product,
                    quantity,
                    unit_price,
                    order_date,
                    status,
                    rejection_reason
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                int(row["order_id"]),
                row["customer_id"],
                row["customer_name"],
                row["product"],
                int(row["quantity"]),
                unit_price,
                row["order_date"],
                row["status"],
                row["rejected_reason"]
            ))

    conn.commit()
    conn.close()

    print("Data loaded successfully into PostgreSQL.")
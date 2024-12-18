from sqlite3 import connect
import re

def get_relevant_data(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT
            c.name,
            c.phone,
            o.ordered,
            oi.sku
        FROM
            customers AS c
            JOIN orders AS o ON c.customerid = o.customerid
            JOIN orders_items AS oi ON oi.orderid = o.orderid
        GROUP BY
            c.name
    """)
    return cur.fetchall()

def find_customer(customers: list[str]) -> list[str]:
    return [customer for customer in customers if re.search(r'BKY\d{4}', customer[3]) and re.search(r'\d{4}-\d{2}-\d{2}\s0[4321]:\d{2}:\d{2}', customer[2])]

if __name__ == "__main__":
    conn = connect('noahs.sqlite')
    customers = get_relevant_data(conn)
    print(find_customer(customers))
    


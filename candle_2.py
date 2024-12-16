from sqlite3 import connect


def get_relevant_data(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT
            c.name,
            c.phone
        FROM 
            customers AS c
            JOIN orders AS o ON c.customerid = o.customerid
            JOIN orders_items AS oi1 ON oi1.orderid = o.orderid
            JOIN products AS p1 ON p1.sku = oi1.sku
            JOIN orders_items AS oi2 ON oi2.orderid = o.orderid
            JOIN products AS p2 ON p2.sku = oi2.sku
        WHERE 
            p1."desc" LIKE '%Bagel%' AND p2."desc" LIKE '%Coffee%';
    """)
    return cur.fetchall()


if __name__ == "__main__":
    conn = connect('noahs.sqlite')
    customers = get_relevant_data(conn)
    print(customers)

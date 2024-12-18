from sqlite3 import connect
import re
from collections import defaultdict


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
    """)
    return cur.fetchall()


def filter_customer(customers: list[tuple]) -> dict:
    customer_dict = defaultdict(int)

    for customer in customers:
        phone = customer[1]
        order_date = customer[2]
        product = customer[3]
        if re.search(r'BKY\d+', product) and re.search(r'\d{4}-\d{2}-\d{2}\s0[4321]:\d{2}:\d{2}', order_date):
            customer_dict[phone] += 1

    return customer_dict

def find_most_active_customer(customer_counts:dict)->str:
    customer = ""
    stored_count = 0
    for phone, count in customer_counts.items():
        if count > stored_count:
            stored_count = count
            customer = phone
    
    return f"phone: {customer}, Count: {stored_count}"


if __name__ == "__main__":
    conn = connect('noahs.sqlite')
    customers = get_relevant_data(conn)

    customer_counts = filter_customer(customers)
    print(find_most_active_customer(customer_counts))





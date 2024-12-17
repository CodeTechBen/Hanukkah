from sqlite3 import connect
import datetime


def get_customer_data(conn):
    cur = conn.cursor()
    cur.execute("""
                SELECT c.name,
                    c.phone,
                    c.birthdate
                FROM customers AS c
                WHERE c.citystatezip = 'Jamaica, NY 11435';
                """)
    return cur.fetchall()

def is_year_of_rabbit(year)-> bool:
    year_of_rabbit = [1939, 1951, 1963, 1975, 1987, 1999, 2011]
    return True if year in year_of_rabbit else False
   
if __name__ == "__main__":
    conn = connect('noahs.sqlite')
    customer = get_customer_data(conn)
    
    customers = []
    for c in customer:
        print(c[2])
from sqlite3 import connect
import re

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


def is_year_of_rabbit(year: str) -> bool:
    year_of_rabbit = ['1939', '1951', '1963', '1975', '1987', '1999', '2011']
    return year in year_of_rabbit


def is_cancer(month: str, day: str) -> bool:
    day = int(day)
    if month == "06" and day >= 21:
        return True
    if month == "07" and day <= 22:
        return True
    return False


if __name__ == "__main__":
    conn = connect('noahs.sqlite')
    customers = get_customer_data(conn)

    for c in customers:
        year = c[2][:4]
        month = c[2][5:7]
        day = c[2][8:]

        if is_year_of_rabbit(year) and is_cancer(month, day):
            print(f"Name: {c[0]}, Phone: {c[1]}, Birthdate: {c[2]}")

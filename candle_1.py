from sqlite3 import connect

def get_relevant_customers(conn) -> list[tuple]:
    cur = conn.cursor()
    cur.execute("""
        SELECT name, phone 
        FROM customers 
        WHERE phone NOT LIKE '%0%'
    """)
    return cur.fetchall()

def format_row(row: tuple[str, str]) -> tuple[str, str]:
    print(row)
    return (row[0].split()[-1].lower(), row[1].replace("-", ""))

def name_to_phone(name):
    phone = ""
    for c in name.lower():
        if c in 'abc':
            phone += '2'
        elif c in 'def':
            phone += '3'
        elif c in 'ghi':
            phone += '4'
        elif c in 'jkl':
            phone += '5'
        elif c in 'mno':
            phone += '6'
        elif c in 'pqrs':
            phone += '7'
        elif c in 'tuv':
            phone += '8'
        elif c in 'wxyz':
            phone += '9'
        else:
            phone += c
    return phone

def find_investigator(customers):
    for name, phone in customers:
        if name_to_phone(name) == phone:
            return name, phone

if __name__ == "__main__":
    conn = connect('noahs.sqlite')
    customers = [format_row(c) for c in get_relevant_customers(conn)]
    investigator_name, investigator_phone = find_investigator(customers)
    
    print(f"Found investigator: {investigator_name} with phone number {investigator_phone}")

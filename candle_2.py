from sqlite3 import connect
def get_relevant_data(conn):
    cur = conn.cursor()
    cur.execute("""QUERY""")
    return cur.fetchall()

if __name__ == "__main__":
    conn = connect('noahs.sqlite')

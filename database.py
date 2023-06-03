import sqlite3

conn = sqlite3.connect('database.db',check_same_thread=False)

def createLoginTable():
    cursor = conn.cursor()

    create_table_query = '''
        CREATE TABLE login (
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    '''

    cursor.execute(create_table_query)

    insert_query = "INSERT INTO login (username, password) VALUES (?, ?)"
    values = ('admin', 'admin')
    cursor.execute(insert_query, values)

    conn.commit()
    conn.close()
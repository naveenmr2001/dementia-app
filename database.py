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

def createRegisterTable():
    cursor = conn.cursor()

    create_table_query = '''
        CREATE TABLE register (
            id TEXT NOT NULL,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            type TEXT NOT NULL
        )
    '''

    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def droptableTable():
    cursor = conn.cursor()

    drop_table_query = '''
        DROP TABLE register;
    '''

    cursor.execute(drop_table_query)

    conn.commit()
    conn.close()
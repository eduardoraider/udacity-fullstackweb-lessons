import psycopg2

conn = psycopg2.connect('dbname=example user=postgres password=123')

# Open a cursor to perform database operations
cursor = conn.cursor()

# create table
# (note: triple quotes allow multiline text in python)
cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')


cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

# commit, so it does the executions on the db and persists in the db
conn.commit()

cursor.close()
conn.close()
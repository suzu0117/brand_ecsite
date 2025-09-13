from connect_db import connect_db

connection = connect_db()

with open("create_table.sql","r") as sql_file:
    sql = sql_file.read()

cursor = connection.cursor()

for query in sql.split(";"):
    if query.strip():
        cursor.execute(query)

connection.commit()
cursor.close()
connection.close()
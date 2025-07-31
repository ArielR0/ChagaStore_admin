import psycopg2

conn = psycopg2.connect(
    dbname = "postgres",
    user= "postgres",
    password= "pg@10",
    host="localhost",
    port= "5432"
)

conn.autocommit = True
cur = conn . cursor()
cur.execute("CREATE DATABASE loja")
cur.close()
conn.close()
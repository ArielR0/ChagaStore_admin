import psycopg2

conn = psycopg2.connect(
    dbname = "loja",
    user= "",
    password= "",
    host="",
    port= ""
)

conn.autocommit = True
cur = conn . cursor()
cur.execute("CREATE DATABASE loja")
cur.close()
conn.close()
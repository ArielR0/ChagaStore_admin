import psycopg2

conn = psycopg2.connect(
    dbname = "loja",
    user= "",
    password= "",
    host="",
    port= ""
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS itens(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    categoria TEXT,
    preco NUMERIC(10,2),
    quantidade INTEGER
            )
 """)

conn.commit()
print("Tabela criada com sucesso.")
cur.close()
conn.close()
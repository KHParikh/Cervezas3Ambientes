import sqlite3
import csv

conn = sqlite3.connect("Cervezas3Ambientes.db")

cur = conn.cursor()

d = {"Neutral.csv":"Neutral", "Calido.csv":"Calido", "Frio.csv":"Frio"}

for key in d:

    with open(key) as f:
        reader = csv.reader(f)
        data = list(reader)

    query = f"""CREATE TABLE {d[key]}(
                ID INTEGER,
                Vasito1 INTEGER,
                Vasito2 INTEGER,
                Vasito3 INTEGER,
                Vasito4 INTEGER,
                Vasito5 INTEGER,
                Vasito6 INTEGER)"""

    cur.execute(query)

    query2 = f"""INSERT INTO {d[key]} (ID, Vasito1, Vasito2, Vasito3, Vasito4, Vasito5, Vasito6) values (?, ?, ?, ?, ?, ?, ?)"""

    for row in data:
        cur.execute(query2, row)

cur.execute("""CREATE TABLE Datos(
            Fecha TEXT,
            Hora TEXT,
            Nombre TEXT,
            ID INTEGER,
            Ambiente TEXT,
            Datos1 INTEGER,
            Datos12 INTEGER,
            Datos2 INTEGER,
            Datos22 INTEGER,
            Datos3 INTEGER,
            Datos32 INTEGER,
            Datos4 INTEGER,
            Datos42 INTEGER,
            Datos5 INTEGER,
            Datos52 INTEGER,
            Datos6 INTEGER,
            Datos62 INTEGER,
            Pulse TEXT,
            GSR TEXT)""")

conn.commit()
conn.close()
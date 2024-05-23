import csv
import psycopg2
from os import listdir

def cargar_datos(archivo_csv, delimitador=';'):
    with open(archivo_csv, newline='') as csvfile:
        lector = csv.reader(csvfile, delimiter=delimitador)
        encabezados = next(lector)  # Leer la primera fila como encabezados
        datos = [fila for fila in lector]
    return encabezados, datos

def crear_tabla(conn, encabezados):
    cur = conn.cursor()
    columnas = ', '.join([f"{header} VARCHAR" for header in encabezados])
    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS calificacion (
        {columnas}
    );
""")
    conn.commit()
    cur.close()

def insertar_datos(conn, encabezados, datos):
    cur = conn.cursor()
    placeholders = ', '.join(['%s'] * len(encabezados))
    columnas = ', '.join(encabezados)
    insert_query = f"INSERT INTO calificacion ({columnas}) VALUES ({placeholders})"
    for fila in datos:
        cur.execute(insert_query, fila)
    conn.commit()
    cur.close()

# Configuración de conexión
conn = psycopg2.connect(dbname="grupo93e2", user="grupo93", password="grupo93", host="pavlov.ing.puc.cl", port=5432)

# Cargar los datos desde el archivo CSV
archivos = listdir('datos e2')
for archivo in archivos:
    encabezados, datos = cargar_datos(f'datos e2/{archivo}')

    # Crear la tabla en la base de datos
    crear_tabla(conn, encabezados)
    

    # Insertar los datos en la tabla
    insertar_datos(conn, encabezados, datos)

    # Cerrar la conexión
conn.close()


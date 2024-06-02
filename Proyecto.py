import csv
import psycopg2
from os import listdir

def cargar_datos(archivo):
    lista = []
    valor_malo=[]
    
    with open(archivo, "r", encoding="latin-1") as data:
        lineas = data.readlines()
    
    is_malo = False
    contador = 0
    
    separador = ";"
    encabezado_separado_por_punto_y_coma = lineas[0].count(";") > 0
    
    if not encabezado_separado_por_punto_y_coma:
        separador = ","

    for i in range(len(lineas)):
        if len(lista) > 1:
            if len(lineas[i].rstrip().split(separador)) == len(lista[0]):
                lista.append(lineas[i].rstrip().split(separador))
                if is_malo:
                    if valor_malo:
                        lista[-1][0] = valor_malo[0][0].join(" ") + lista[-1][0]
                        is_malo = False
                        valor_malo = []
            else:
                valor_malo.append(lineas[i].rstrip().split(separador))
                is_malo = True
        else:
            lista.append(lineas[i].rstrip().split(separador))
        contador += 1
    
    return [i.replace("\"", "").replace("'", "") for i in lista[0]], lista[1::]

def carga_insercion_datos(conection, tipo_de_consulta, consulta, datos=None):
    db_connection = psycopg2.connect(
        dbname=conection[0],
        user=conection[1],
        password=conection[2],
        host=conection[3],
        port=conection[4]
    )
    
    cur = db_connection.cursor()
    
    if tipo_de_consulta == "CREATE":
        query = consulta
        try:
            cur.execute(query)
        except psycopg2.OperationalError as e:
            print(e)
    elif tipo_de_consulta == "INSERT":
        query = consulta
        try:
            if datos:
                for dato in datos:
                    cur.execute(query, dato)
        except psycopg2.OperationalError as e:
            print(e)
    elif tipo_de_consulta == "CONSULT":
        query = consulta
        try:
            cur.execute(query)
        except psycopg2.OperationalError as e:
            print(e)
    
    db_connection.commit()
    db_connection.close()

# Configuración de conexión
info_connect = ["grupo93e2", "grupo93", "grupo93", "pavlov.ing.puc.cl", 5432]

# Cargar los datos desde el archivo CSV
archivos = listdir('datos e2')

for archivo in archivos:
    encabezados, datos = cargar_datos(f'datos e2/{archivo}')
    columnas = ', '.join([f"{col} TEXT" for col in encabezados])
    tabla = archivo.split(".")[0]
    c_query = f"CREATE TABLE IF NOT EXISTS {tabla} ({columnas});"
    carga_insercion_datos(info_connect, "CREATE", c_query)
    
    placeholder = ', '.join(['%s'] * len(encabezados))
    i_query = f"INSERT INTO {tabla} ({', '.join(encabezados)}) VALUES ({placeholder})"
    carga_insercion_datos(info_connect, "INSERT", i_query, datos)

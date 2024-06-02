import psycopg2

def carga_insercion_datos(conection:list, tipo_de_consulta, consulta:str):    
    db_connection = psycopg2.connect(
        dbname=conection[0],
        user=conection[1],
        password=conection[2],
        host=conection[3],
        port=conection[4])
    
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
            cur.execute(query)
        except psycopg2.OperationalError as e:
            print(e)
    elif tipo_de_consulta == "CONSTULT": 
        query = consulta
        try:
            cur.execute(query)
        except psycopg2.OperationalError as e:
            print(e)    
    db_connection.commit()
    db_connection.close()
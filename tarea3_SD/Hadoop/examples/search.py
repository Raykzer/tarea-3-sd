import json
import os
import psycopg2
import re


def insert_data(cursor):
    print("Insertando archivos...")
    with open('outhadoop/part-00000', 'r') as archivo:
        next(archivo)
        for linea in archivo:
            datos = re.findall(r'\b\w+\b|\([^)]*\)', linea)

            letra = datos[0]
            pares = [tuple(map(int, par.strip('()').split(' '))) for par in datos[1:]]
            for n, m in pares:
                cursor.execute(
                    "INSERT INTO registros (palabra, documento, frecuencia) VALUES (%s, %s, %s) ON CONFLICT (palabra, documento) DO NOTHING",
                    (letra, n, m))

            connection.commit()

def search_word(cursor):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nGooglent")
    palabra = input("Buscar: ")

    query = f"SELECT documento, frecuencia, url FROM paginas INNER JOIN registros ON paginas.id = registros.documento WHERE palabra = '{palabra}' ORDER BY frecuencia DESC LIMIT 5"
    cursor.execute(query)

    resultados = cursor.fetchall()
    resultados_json = []
    column_names = [desc[0] for desc in cursor.description]

    for fila in resultados:
        fila_json = dict(zip(column_names, fila))
        resultados_json.append(fila_json)

    print(json.dumps(resultados_json, indent=2))

connection = psycopg2.connect(user="postgres",
                              password="postgres",
                              host="db",
                              port="5432",
                              database="tarea")

try:
    cursor = connection.cursor()
    insert_data(cursor)
    search_word(cursor)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


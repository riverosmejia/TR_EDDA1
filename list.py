import psycopg2

from grafo import GrafoDirigido

from persona import persona

from mensaje import relacion

db_params = {
    "host": "bubble.db.elephantsql.com",
    "user": "fpaowvnx",
    "password": "nS0nUBYZf8hWYIwYlnNDxa7Io1kLhUlv",
    "port": 5432,
    "database": "fpaowvnx",
}

if __name__ == "__main__":

    grafo = GrafoDirigido()

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Ejemplo: Obtener todas las filas de la tabla
        cursor.execute("SELECT * FROM tablaproyecto")
        rows = cursor.fetchall()

        cont=0

        # Mostrar resultados
        for row in rows:

            print(cont)

            cont=cont+1

            if not grafo.encontrar_persona(row[0]):

                rogue=persona(row[0],row[1])                

                grafo.agregar_nodo(rogue)

            if not grafo.encontrar_persona(row[3]):

                rogue1=persona(row[3],row[4])                

                grafo.agregar_nodo(rogue1)

            grafo.agregar_arista(row[0],row[3],row[2],row[5])

        for cacatua in grafo.relaciones:

            cacatua.obtener_info()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión
        try:
            if connection:
                cursor.close()
                connection.close()
                print("Conexión cerrada.")
        except NameError:
            # En caso de que haya un error antes de definir 'connection'
            pass
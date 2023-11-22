import os
import platform
import psycopg2

from grafo import Grafo
from persona import persona
from mensaje import relacion

def limpiar_pantalla():
    sistema_operativo = platform.system()
    
    if sistema_operativo == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def pausar_pantalla():
    input('Presiona Enter para continuar...')


db_params = {
    "host": "bubble.db.elephantsql.com",
    "user": "fpaowvnx",
    "password": "nS0nUBYZf8hWYIwYlnNDxa7Io1kLhUlv",
    "port": 5432,
    "database": "fpaowvnx",
}

if __name__ == "__main__":

    grafo = Grafo()

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Ejemplo: Obtener todas las filas de la tabla
        cursor.execute("SELECT * FROM tablaproyecto")
        rows = cursor.fetchall()

        for row in rows:

            if not grafo.encontrar_persona(row[0]):

                rogue=persona(row[0],row[1])                

                grafo.agregar_nodo(rogue)

            if not grafo.encontrar_persona(row[3]):

                rogue1=persona(row[3],row[4])                

                grafo.agregar_nodo(rogue1)

            grafo.agregar_arista(row[0],row[3],row[2],row[5])

        cerrar=False

        while cerrar is not True:

            pausar_pantalla()

            limpiar_pantalla()

            resp = int(input('1.Mostrar personas\n2.mostrar mensajes\n3.mostrar Relaciones\n4.encontrar mejor amigo\n5.cerrar programa\nR/='))

            print('<---------------------->')

            if resp==1:

                grafo.mostrar_personas()

            elif resp==2:

                cont1=0

                for row1 in rows:

                    cont1+=1
                    print(f'{cont1}. mensaje: {row1[2]} ---------------> hora: {row1[5]}')

            elif resp==3:

                cont1=0

                for cacatua in grafo.relaciones:

                    cont1+=1

                    print(f'{cont1}.')

                    cacatua.obtener_info()

            elif resp == 4:
            
                persona_id = int(input("Ingrese el teléfono de la persona para ver su mayor relación: "))
                grafo.persona_con_mas_relacion(persona_id)

            elif resp == 5:

                cerrar=True

            print('<---------------------->')

            pausar_pantalla()

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
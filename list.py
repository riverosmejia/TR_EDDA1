import psycopg2

# Parámetros de conexión a la base de datos
db_params = {
    "host": "bubble.db.elephantsql.com",
    "user": "fpaowvnx",
    "password": "nS0nUBYZf8hWYIwYlnNDxa7Io1kLhUlv",  # Usa tu clave API en lugar de la contraseña
    "port": 5432,
    "database": "fpaowvnx",
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Ejemplo: Obtener todas las filas de la tabla
    cursor.execute("SELECT * FROM tablaproyecto")
    rows = cursor.fetchall()

    # Mostrar resultados
    for row in rows:
        print(row)

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
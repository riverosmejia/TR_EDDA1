# TR_EDDA1

<--Guía completa que incluye todos los pasos desde la instalación de las dependencias hasta la carga de datos en ElephantSQL, para los sistemas operativos Linux, Windows y macOS-->

Paso 1: Instalar psycopg2:

    pip install psycopg2-binary

Paso 2: Descargar e Instalar pgloader (Solo si aún no lo tienes):
    
    Linux:
        
        sudo apt-get install pgloader
    
    Windows:
        
        Descarga el instalador desde la página de descargas de pgloader y sigue las instrucciones.

    macOS:

        brew install pgloader
    
    
Paso 3: Conexión y Manipulación de la Base de Datos desde Python:

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

    <--NOTA: PARA QUE FUNCIONE HAY QUE ACTIVAR EL ENTORNO VIRTUAL-->

        para activar un entorno virtual, puedes proporcionar comandos simples para los usuarios. Aquí tienes un ejemplo para Linux, Windows y macOS:

            Para Linux y macOS:
            bash
            Copy code
            # Crear un entorno virtual
            python3 -m venv nombre_del_entorno

            # Activar el entorno virtual
            source nombre_del_entorno/bin/activate

            # Desactivar el entorno virtual
            deactivate
            Para Windows:
            bash
            Copy code
            # Crear un entorno virtual
            python -m venv nombre_del_entorno

            # Activar el entorno virtual
            nombre_del_entorno\Scripts\activate

            # Desactivar el entorno virtual
            deactivate


Paso 4: Utilizar pgloader para Cargar Datos en ElephantSQL:

pgloader mysql://usuario:contraseña@localhost/baseproyecto \

         postgresql://tu_usuario:tu_contraseña@bubble.db.elephantsql.com:5432/tu_base_de_datos \
         -S nombre_del_archivo.sql

Paso 5: Verificación en ElephantSQL:

Accede a tu cuenta en ElephantSQL y verifica que la base de datos y los datos se hayan cargado correctamente.

Recuerda reemplazar "tu_usuario", "tu_contraseña" y "tu_base_de_datos" con las credenciales correctas de tu instancia ElephantSQL.
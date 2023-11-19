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
        "user": "tu_usuario",
        "password": "tu_contraseña",
        "port": 5432,
        "database": "tu_base_de_datos",
    }

    # Conexión a la base de datos
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
        if connection:
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

Paso 4: Utilizar pgloader para Cargar Datos en ElephantSQL:

pgloader mysql://usuario:contraseña@localhost/baseproyecto \

         postgresql://tu_usuario:tu_contraseña@bubble.db.elephantsql.com:5432/tu_base_de_datos \
         -S nombre_del_archivo.sql

Paso 5: Verificación en ElephantSQL:

Accede a tu cuenta en ElephantSQL y verifica que la base de datos y los datos se hayan cargado correctamente.

Recuerda reemplazar "tu_usuario", "tu_contraseña" y "tu_base_de_datos" con las credenciales correctas de tu instancia ElephantSQL.
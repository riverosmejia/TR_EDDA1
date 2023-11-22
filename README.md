Este repositorio contiene un proyecto que te permite acceder a datos desde una base de datos PostgreSQL en Elephant SQL sin la necesidad de utilizar MySQL. A continuación, se detallan los pasos para configurar el entorno virtual, instalar las librerías necesarias (`psycopg2` y `platform`), y extraer datos de la base de datos.

## Instalación y Configuración del Entorno Virtual

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/tu-proyecto.git
   cd tu-proyecto
Crea un entorno virtual (asegúrate de tener virtualenv instalado):

bash
Copy code
virtualenv venv
Activa el entorno virtual:

En Windows:
bash
Copy code
venv\Scripts\activate
En Linux/Mac:
bash
Copy code
source venv/bin/activate
Instala las dependencias del proyecto:

bash
Copy code
pip install -r requirements.txt
Nota: Si encuentras problemas al intentar instalar las librerías, asegúrate de que el entorno virtual esté activado.

Descargar Librerías
Para descargar las librerías necesarias, ejecuta el siguiente comando:

bash
Copy code
pip install psycopg2 platform
Nota: Si encuentras problemas al descargar las librerías, asegúrate de que el entorno virtual esté activado.

Configuración de la Base de Datos
En el archivo config.py, asegúrate de proporcionar la información correcta de tu base de datos PostgreSQL en Elephant SQL.

python
Copy code
# config.py

DATABASE_CONFIG = {
    'host': 'tu-host',
    'database': 'tu-base-de-datos',
    'user': 'tu-usuario',
    'password': 'tu-contraseña',
    'port': 'tu-puerto',
}
Uso del Script para Extraer Datos
Ejecuta el script extract_data.py para extraer datos de la base de datos:

bash
Copy code
python extract_data.py
Esto iniciará el proceso de extracción y mostrará los datos obtenidos.

Notas Importantes
Si encuentras problemas al descargar las librerías, asegúrate de que el entorno virtual esté activado. Puedes activarlo utilizando el comando source venv/bin/activate en Linux/Mac o venv\Scripts\activate en Windows.

En la carpeta dist del proyecto, encontrarás ejecutables para Windows (tu-proyecto.exe), Linux (tu-proyecto), y macOS (tu-proyecto). Utiliza el ejecutable correspondiente según tu sistema operativo para ejecutar el programa.

¡Listo! Ahora deberías poder acceder y extraer datos de tu base de datos PostgreSQL en Elephant SQL sin necesidad de MySQL. ¡Disfruta del proyecto!
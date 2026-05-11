import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_conexion():
    try:
        # Aquí se implementa la conexión física
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        
        if conexion.is_connected():
            print("✅ Conectado exitosamente a MySQL")
            return conexion

    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

# Prueba rápida
if __name__ == "__main__":
    con = obtener_conexion()
    if con:
        con.close()
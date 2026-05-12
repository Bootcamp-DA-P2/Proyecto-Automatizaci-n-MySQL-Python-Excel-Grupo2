import pandas as pd
import sys
from datetime import datetime
from pathlib import Path
import sqlalchemy
import mysql.connector
import openpyxl
from dotenv import load_dotenv

# Configurar el path para encontrar el contenido de src
sys.path.insert(0, str(Path(__file__).parent / 'src'))

# Ahora podemos importar de forma limpia
try:
    from sakila_ETL import proceso_completo
    from conexion import obtener_conexion
except ImportError as e:
    print(f"❌ Error crítico de importación: {e}")
    sys.exit(1)

def test_conexion_inicial():
    """Usa la lógica de conexion.py para validar el acceso"""
    con = obtener_conexion()
    if con:
        con.close()
        return True
    return False

def main():
    print("\n" + "="*50)
    print("🚀 PROCESO DE AUTOMATIZACIÓN SAKILA")
    print("="*50)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print("PASO 1: Probando conexión a MySQL...")
    if not test_conexion_inicial():
        print("❌ No se puede conectar a MySQL. Revisa el .env")
        return False

    print("\nPASO 2: Ejecutando proceso ETL...")
    if proceso_completo():
        print("\n✅ PROCESO COMPLETADO")
        print(f"\n📂 Archivos generados en 'output/':")
        print("   • Dataframe_1_Clientes.csv")
        print("   • Dataframe_2_CatalogoPeliculas.csv")
        print("   • Dataframe_3_Elenco_Popularidad.csv")
        print("   • Dataframe_4_amount.csv")
        print("\n💾 CSVs listos para cargar en Power Query")
    else:
        print("\n❌ ERROR EN EL PROCESO")
        print("\n💡 Posibles causas:")
        print("   1. MySQL no está corriendo")
        print("   2. Credenciales incorrectas en .env")
        print("   3. Base de datos 'sakila' no existe")
        return False

    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Proceso interrumpido")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    finally:
        input("\nPresiona ENTER para salir...")
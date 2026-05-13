# Proyecto de Automatizacion-MySQL-Python-Excel-Grupo2
## 👥 Equipo — Grupo 2

| Nombre | Rol |
|---|---|
| Sonia Navarro | Queries SQL y visualizaciones |
| María Bejarano | Dashboard Excel y transformación de datos |
| Romina Navea | Desarrollo ETL y conexión base de datos |

---

## 📋 Descripción del proyecto

Este proyecto automatiza la extracción y análisis de datos de la base de datos **Sakila** usando Python, generando 4 datasets en formato CSV que se conectan automáticamente a un libro de Excel con tablas dinámicas y KPIs.

**Enfoque híbrido:** automatización del flujo y carga de datos + diseño manual en Excel.

---

## 🗄️ Base de datos

**Sakila** es una base de datos de ejemplo de MySQL que simula el sistema de una tienda de alquiler de películas. Contiene datos de:

- Clientes y direcciones
- Películas, categorías e idiomas
- Actores y elenco
- Alquileres y pagos
- Inventario y tiendas

---

## 📊 Análisis realizado

- **Clientes VIP** → ranking de clientes por total pagado
- **Ingresos por país** → distribución geográfica de ingresos
- **Categorías más alquiladas** → popularidad por género de película
- **Clientes activos vs inactivos** → estado de clientes por país

---

## 🗂️ Estructura del proyecto

```
proyecto-sakila-automation/
│
├── main.py                          ⭐ EJECUTAR ESTE
│
├── src/
│   ├── __init__.py
│   ├── sakila_ETL.py                (extracción y transformación)
│   ├── config.py                    (configuración desde .env)
│   └── test_conexion.py             (prueba de conexión MySQL)
│
├── queries/
│   ├── Dataframe_1_Clientes.sql
│   ├── Dataframe_2_CatalogoPeliculas.sql
│   ├── Dataframe_3_Elenco_Popularidad.sql
│   └── Dataframe_4_amount.sql
│
├── output/                          (CSVs generados automáticamente)
│   ├── Dataframe_1_Clientes.csv
│   ├── Dataframe_2_CatalogoPeliculas.csv
│   ├── Dataframe_3_Elenco_Popularidad.csv
│   └── Dataframe_4_amount.csv
│
├── dashboard/
│   └── Sakila_Dashboard.xlsx
│
├── requirements.txt
├── .env                             🔒 NO subir a GitHub
├── .env.example
├── .gitignore
└── README.md
```

---

## 🧰 Tecnologías utilizadas

- **Python 3**
- **MySQL** + base de datos Sakila
- **pandas** — manipulación de datos
- **sqlalchemy** — conexión a base de datos
- **mysql-connector-python** — driver MySQL
- **openpyxl** — generación de archivos Excel
- **python-dotenv** — gestión de variables de entorno
- **Excel** — tablas dinámicas y dashboard
- **Git & GitHub** — control de versiones

---

## ⚙️ Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/Bootcamp-DA-P2/Proyecto-Automatizaci-n-MySQL-Python-Excel-Grupo2.git
cd Proyecto-Automatizaci-n-MySQL-Python-Excel-Grupo2
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

**Windows (Git Bash):**
```bash
source .venv/Scripts/activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Copia el archivo `.env.example` y renómbralo a `.env`:

```bash
cp .env.example .env
```

Edita el `.env` con tus credenciales de MySQL:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=sakila
```

### 6. Ejecutar el proyecto

```bash
.venv/Scripts/python.exe main.py
```

Esto generará automáticamente los 4 CSVs en la carpeta `/output`.

### 7. Actualizar el Excel

Abre `dashboard/Sakila_Dashboard.xlsx` y ve a:
```
Datos → Actualizar todo
```

---

## 📈 KPIs del dashboard

| KPI | Descripción |
|---|---|
| Total ingresos | Suma de todos los pagos |
| Total clientes | Número de clientes registrados |
| Clientes activos | Clientes con estado activo |
| Total películas | Ingreso promedio por cliente | 

---

## 🔒 Seguridad

El archivo `.env` contiene credenciales privadas y **nunca se sube a GitHub**. Está protegido por `.gitignore`.

Usa `.env.example` como plantilla para configurar tus propias credenciales.

---

## 💡 Solución de problemas

**Error: No module named 'pandas'**
```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

**Error: Access denied for user**
Revisa que las credenciales en el `.env` son correctas.

**Error: No database selected**
Asegúrate de que `DB_NAME=sakila` está en el `.env` y que la base de datos Sakila está instalada en MySQL.

**Error: Commands out of sync**
Verifica que los archivos `.sql` en `/queries` no tienen `USE sakila;` al principio.

---

## 📚 Recursos

- [Documentación Sakila](https://dev.mysql.com/doc/sakila/en/)
- [pandas](https://pandas.pydata.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

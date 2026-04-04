# Semana 2: Arquitecturas de Datos y MongoDB

## 1. Ejercicios Complementarios

### Ejercicio 1: Consultas SQL
| id | nombre | departamento | salario |
| -- | ---------- | ------------ | ------- |
| 1 | Juan | IT | 50000 |
| 2 | María | HR | 45000 |
| 3 | Carlos | IT | 55000 |
| 4 | Ana | Finanzas | 48000 |
| 5 | Pedro | Marketing | 42000 |

**Solución:**
```sql
SELECT * FROM empleados;

SELECT nombre, salario 
FROM empleados 
WHERE departamento = 'IT';

SELECT * 
FROM empleados 
ORDER BY salario DESC 
LIMIT 1;

SELECT departamento, COUNT(*) 
FROM empleados 
GROUP BY departamento;

UPDATE empleados 
SET salario = 50000 
WHERE nombre = 'María';
```

### Ejercicio 2: Joins

**empleados**
| id | nombre | id_departamento |
| -- | -------- | ---------------- |
| 1 | Juan | 1 |
| 2 | María | 2 |
| 3 | Carlos | 1 |
**departamentos**
| id | nombre |
| -- | ----------- |
| 1 | IT |
| 2 | HR |
| 3 | Finanzas |
Escribir consultas para:
1. INNER JOIN entre empleados y departamentos
2. LEFT JOIN mostrando todos los empleados
3. Contar empleados por departamento

**solucion**

``` sql
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d
ON e.id_departamento = d.id;

SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d
ON e.id_departamento = d.id;

SELECT d.nombre, COUNT(e.id)
FROM departamentos d
LEFT JOIN empleados e
ON e.id_departamento = d.id
GROUP BY d.nombre;
```
### Ejercicio 3: Manipulación de JSON

```json
{
"empleados": [
{"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
{"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
{"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
]
}
```
1. Extraer los nombres de todos los empleados
2. Agregar una nueva habilidad a Juan
3. Crear un nuevo empleado con id: 4
4. Eliminar las habilidades de María

***solucion***
```python
data = {
"empleados": [
{"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
{"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
{"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
]
}

# Nombres
nombres = [e["nombre"] for e in data["empleados"]]

# Agregar habilidad
data["empleados"][0]["habilidades"].append("Machine Learning")

# Nuevo empleado
data["empleados"].append({
"id": 4,
"nombre": "Luis",
"habilidades": ["SQL"]
})

# Eliminar habilidades
del data["empleados"][1]["habilidades"]
```
### Ejercicio 4: Estructuras de Datos en Python

```python
# Lista de diccionarios (simulando una tabla)
empleados = [
{"id": 1, "nombre": "Juan", "salario": 50000},
{"id": 2, "nombre": "María", "salario": 45000},
{"id": 3, "nombre": "Carlos", "salario": 55000}
]
# Ejercicios:
# 1. Agregar un nuevo empleado
# 2. Buscar empleado por id
# 3. Calcular promedio de salarios
# 4. Filtrar empleados con salario > 50000
# 5. Actualizar el nombre del empleado con id=2
```
***solucion***
```python
empleados = [
{"id": 1, "nombre": "Juan", "salario": 50000},
{"id": 2, "nombre": "María", "salario": 45000},
{"id": 3, "nombre": "Carlos", "salario": 55000}
]

empleados.append({"id": 4, "nombre": "Luis", "salario": 47000})

empleado = next(e for e in empleados if e["id"] == 1)

promedio = sum(e["salario"] for e in empleados) / len(empleados)

altos = [e for e in empleados if e["salario"] > 50000]

for e in empleados:
    if e["id"] == 2:
        e["nombre"] = "Maria Actualizada"
```

### Ejercicio 5: Operaciones CRUD

```javascript
// Insertar documentos
db.productos.insertMany([
{"nombre": "Laptop", "precio": 999, "categoria": "Electrónica"},
{"nombre": "Mouse", "precio": 29, "categoria": "Electrónica"},
{"nombre": "Escritorio", "precio": 299, "categoria": "Muebles"}
])
// Realizar las siguientes operaciones:
# 1. Read: Encontrar todos los productos de Electrónica
# 2. Read: Encontrar productos con precio < 100
# 3. Update: Aumentar precio de Laptop en 10%
# 4. Delete: Eliminar productos con precio < 50
# 5. Create: Agregar un nuevo producto
```
***solucion***

```javascript
db.productos.find({categoria: "Electrónica"})

db.productos.find({precio: {$lt: 100}})

db.productos.updateOne(
  {nombre: "Laptop"},
  {$mul: {precio: 1.1}}
)

db.productos.deleteMany({precio: {$lt: 50}})

db.productos.insertOne({
  nombre: "Teclado",
  precio: 49,
  categoria: "Electrónica"
})
```

### Ejercicio 6: Consultas Avanzadas en MongoDB

```javascript
// Colección: estudiantes
{"nombre": "Ana", "materias": ["Math", "Physics"], "edad": 20}
{"nombre": "Luis", "materias": ["Math", "Chemistry"], "edad": 22}
{"nombre": "Sofia", "materias": ["Biology"], "edad": 19}
# Consultas:
# 1. Encontrar estudiantes que cursan Math
# 2. Encontrar estudiantes mayores de 20
# 3. Contar estudiantes por edad
# 4. Proyectar solo nombres
```

### Ejercicio 7: Tipos de Bases de Datos NoSQL

**Solución:**

Las bases de datos NoSQL se clasifican en distintos tipos según la forma en que almacenan y organizan la información.

---

#### 1. Bases de datos documentales (MongoDB, CouchDB)

Estas bases de datos almacenan la información en documentos con formato similar a JSON.

**¿Cuándo usarlas?**
- Cuando los datos no tienen una estructura fija
- Aplicaciones web modernas
- Sistemas con cambios frecuentes en la estructura de datos

**Ventajas:**
- Flexibilidad en el esquema
- Fácil escalabilidad
- Integración natural con aplicaciones en JavaScript/Python

**Desventajas:**
- Puede haber redundancia de datos
- Menor control en relaciones complejas

#### 2. Bases de datos Key-Value (Redis, DynamoDB)

Almacenan datos en forma de pares clave-valor, como un diccionario.

**¿Cuándo usarlas?**
- Sistemas que requieren alta velocidad
- Caché de datos
- Sesiones de usuarios

**Ventajas:**
- Muy rápidas
- Simples de usar
- Alto rendimiento

**Desventajas:**
- No permiten consultas complejas
- Estructura limitada

#### 3. Bases de datos columnar (Cassandra, HBase)

Organizan los datos en columnas en lugar de filas.

**¿Cuándo usarlas?**
- Big Data
- Sistemas distribuidos
- Análisis de grandes volúmenes de datos

**Ventajas:**
- Alta escalabilidad
- Buen rendimiento en consultas analíticas
- Manejo eficiente de grandes datos

**Desventajas:**
- Complejas de implementar
- Requieren mayor conocimiento técnico

#### 4.Bases de datos de grafos (Neo4j)

Almacenan datos en forma de nodos y relaciones.

**¿Cuándo usarlas?**
- Redes sociales
- Sistemas de recomendación
- Análisis de relaciones complejas

**Ventajas:**
- Excelente manejo de relaciones
- Consultas eficientes para grafos
- Ideal para datos conectados

**Desventajas:**
- No son ideales para datos simples
- Escalabilidad más compleja en algunos casos

### Ejercicio 8: Arquitecturas de Almacenamiento

**Solución:**

#### 1. ¿Qué es un Data Lake?

Un Data Lake es un sistema de almacenamiento que permite guardar grandes volúmenes de datos en su formato original, sin necesidad de estructurarlos previamente.

**Características:**
- Almacena datos crudos (sin procesar)
- Soporta datos estructurados, semi-estructurados y no estructurados
- Alta escalabilidad

**¿Cuándo se usa?**
- Análisis de Big Data
- Machine Learning
- Procesamiento de grandes volúmenes de información

#### 2. ¿Qué es un Data Warehouse?

Un Data Warehouse es un sistema de almacenamiento que guarda datos estructurados y organizados, optimizados para análisis y generación de reportes.

**Características:**
- Datos limpios y organizados
- Orientado a consultas analíticas
- Información histórica

**¿Cuándo se usa?**
- Business Intelligence
- Reportes empresariales
- Análisis de tendencias

#### 3. Diferencias entre OLAP y OLTP

**OLTP (Online Transaction Processing):**
- Maneja operaciones diarias
- Transacciones rápidas (insertar, actualizar, eliminar)
- Ejemplo: sistemas bancarios, ventas en línea

**OLAP (Online Analytical Processing):**
- Enfocado en análisis de datos
- Consultas complejas
- Ejemplo: análisis de ventas, reportes estratégicos

#### 4. ¿Qué es ETL?

ETL significa **Extract, Transform, Load** (Extraer, Transformar y Cargar).

**Fases:**

1. **Extract (Extraer):**
   Se obtienen datos de diferentes fuentes (bases de datos, archivos, APIs).

2. **Transform (Transformar):**
   Se limpian, organizan y preparan los datos.

3. **Load (Cargar):**
   Se almacenan en un sistema como Data Warehouse o Data Lake.

## Actividades Prácticas
Actividad 2.1: Arquitecturas de Datos

Entregable: Investigación sobre tipos de arquitecturas de almacenamiento y sus aplicaciones.

Actividad 2.2: Introducción a MongoDB

Entregable: Creación de base de datos, colección y carga de documentos utilizando MongoDB Compass y Python.

Actividad 2.3: Operaciones CRUD

Entregable: Implementación de operaciones Create, Read, Update y Delete en MongoDB mediante Python.

Actividad 2.4: Modelado NoSQL

Entregable: Diseño de un modelo de datos para biblioteca digital utilizando colecciones y documentos en formato JSON.

## Resumen de Aprendizaje
- Comprendí las diferencias entre bases de datos SQL y NoSQL
- Aprendí a utilizar MongoDB para almacenamiento de datos
- Implementé operaciones CRUD con Python
- Desarrollé habilidades en manejo de JSON
- Entendí cómo modelar datos en sistemas NoSQL

### Referencias
- Documentación oficial de MongoDB
- Documentación de Python
- Material de clase

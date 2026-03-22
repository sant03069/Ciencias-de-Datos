# Semana 1: Fundamentos de Ciencia de Datos y Big Data

## 1. Ejercicios Complementarios

### Ejercicio 1:
**Solución:**

a) 3x + 5 = 17      
→ x = 4
3x = 17-5
3x = 12
x = 12/3
x = 4

b) 2y - 8 = 22     
→ y = 15
2y = 22 + 8
2y = 30
y = 30/2
y = 15

c) 4z + 3 = 3z + 10     
→ z = 7
4z - 3z + 3 = 10
z + 3 = 10
z + 3 - 3 = 10 - 3
z = 7

d) 5(x + 2) = 35    
→ x = 5
(x + 2) = 35/5
x + 2  = 7
x = 7 - 2
x = 5

### Ejercicio 2: Funciones Lineales
**Solución:**

Función: f(x) = 2x + 3
                        |f(x) |  Y  |
                        |-----------|
f(0) = 2·0 + 3 = 3      |  0  |  3  |
f(1) = 2·1 + 3 = 5      |  1  |  5  |
f(5) = 2·5 + 3 = 13     |  5  |  13 |
f(10) = 2·10 + 3 = 23   |  10 |  23 |

|f(x) |  Y  |
|-----------|
|  0  |  3  |
|  1  |  5  |
|  5  |  13 |
|  10 |  23 |


### Ejercicio 3: Escalas y Volúmenes (Big Data)
**Solución:**

Expresar en notación científica:

| Cantidad                    | Notación Científica |
| --------------------------- | ------------------- |
| 1,000,000 bytes             | 1 × 10⁶ bytes      |
| 1,000,000,000 registros     | 1 × 10⁹ registros  |
| 1,000,000,000,000 bytes     | 1 × 10¹² bytes     |

### Ejercicio 4: Diagrmas de Flujo
**Solución:**

<img width="1127" height="1218" alt="Captura de pantalla 2026-03-21 112933" src="https://github.com/user-attachments/assets/62994ca0-878d-496c-acdc-24c5b0b59bae" />

<img width="933" height="1185" alt="Captura de pantalla 2026-03-21 113917" src="https://github.com/user-attachments/assets/149c1a6b-8ffb-4b10-ba21-fe5dcd781575" />

![Diagrama de flujo](https://github.com/user-attachments/assets/22cffb95-6cd9-4486-85cc-a0fd6cafbce1)


### Ejercicio 5: Pseudocódigo
**Solución:**
<img width="799" height="503" alt="Captura de pantalla 2026-03-21 165314" src="https://github.com/user-attachments/assets/fb5ec4dd-163b-46bb-9497-a5dabb50ca74" />

<img width="713" height="1128" alt="Captura de pantalla 2026-03-21 165339" src="https://github.com/user-attachments/assets/c7e0fa3a-526c-40a0-a415-ff442566a68c" />

<img width="726" height="997" alt="Captura de pantalla 2026-03-21 165426" src="https://github.com/user-attachments/assets/032e4d87-bc7c-4d11-b159-366ac3bb332d" />

### Ejercicio 6: Operaciones Booleanas
**Solución:**

```
a = True
b = False
c = True

print(a and b)        # False
print(a or b)         # True
print(not b)          # True
print(a and c)        # True
print((a or b) and c) # True

```

### Ejercicio 7: Historia de la Ciencia de Datos
**Solución:**

**1. ¿Quién es considerada la primera científica de datos?**  
Florence Nightingale es considerada la primera científica de datos por su uso de estadísticas y visualización de datos para mejorar la salud pública.

**2. ¿Qué es el "Data Science Venn Diagram" de Drew Conway?**  
Es un diagrama que muestra la intersección de tres áreas clave:
- Programación (hacking skills)
- Matemáticas y estadística
- Conocimiento del dominio  

El verdadero científico de datos se encuentra en la intersección de estas tres habilidades.

**3. Menciona 3 herramientas modernas de Big Data**
- Apache Hadoop  
- Apache Spark  
- Tableau

### Ejercicio 8: Aplicaciones de Big Data
**Solución:**

**Salud:**  
El Big Data se utiliza para analizar historiales médicos y detectar enfermedades de forma temprana, como el cáncer, mediante algoritmos predictivos.

**Finanzas:**  
Se usa para detectar fraudes en transacciones bancarias en tiempo real, analizando patrones de comportamiento de los usuarios.

**Redes sociales:**  
Plataformas como Facebook o Instagram utilizan Big Data para recomendar contenido personalizado basado en tus intereses y comportamiento.

**Deportes:**  
Equipos deportivos analizan el rendimiento de los jugadores mediante datos (velocidad, resistencia, estadísticas) para mejorar estrategias y prevenir lesiones.

## 2. Actividades Prácticas

### Actividad 1.1: Conceptos Fundamentales
**Entregable:** Documento con definiciones clave de ciencia de datos, Big Data, machine learning y análisis de datos.

### Actividad 1.2: Casos de Uso
**Entregable:** Documento describiendo diferentes aplicaciones de ciencia de datos en negocios, salud, deportes y finanzas.

### Actividad 1.3: Entorno de Trabajo
**Entregable:** Script en Python (`cuaderno Jupyter.py`) que lee archivos CSV y verifica funcionamiento de librerías; se resolvieron problemas de permisos y rutas.

### Actividad 1.4: Fuentes de Datos
**Entregable:** Markdown (`Actividad1.4.md`) describiendo qué es Kaggle, exploración de 3 datasets públicos y análisis del dataset Titanic con preguntas posibles.

## 3. Resumen de Aprendizaje

- Aprendí a configurar un entorno de desarrollo funcional con Python y Git.  
- Comprendí cómo explorar y analizar datasets reales en Kaggle.  
- Pude resolver problemas típicos de permisos y rutas al trabajar con archivos locales.  
- Consolidé conocimiento sobre la estructura de commits y documentación semanal.

## 4. Dudas o Preguntas

- ¿Hay alguna recomendación para automatizar la verificación de librerías instaladas en Python?  
- ¿Se puede hacer un flujo seguro en Git que evite errores de “fetch first” automáticamente?

## 5. Referencias

- [Kaggle](https://www.kaggle.com/) – Plataforma para datasets y competencias de ciencia de datos.  
- [Documentación oficial de pandas](https://pandas.pydata.org/docs/) – Lectura y manipulación de datos en Python.  

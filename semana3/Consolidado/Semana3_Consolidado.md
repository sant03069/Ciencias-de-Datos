# Semana 3: Python para Ciencia de Datos y EDA

## 1. Ejercicios Complementarios


### Ejercicio 1: Variables y Tipos de Datos

**Solución:**
```python
entero = 10
flotante = 10.5
texto = "Hola"
booleano = True
lista = [1, 2, 3]
diccionario = {"nombre": "Juan", "edad": 20}

num_str = "25"
num_int = int(num_str)
num_float = float(num_int)

edad = 20
print(f"El usuario tiene {edad} años")
```

### Ejercicio 2: Control de Flujo

**Solución:**
```python
num = -5
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")

opcion = 1
if opcion == 1:
    print("Opción 1")
elif opcion == 2:
    print("Opción 2")
else:
    print("Otra opción")

lista = [1, 2, 3]
for i in lista:
    print(i)

n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(factorial)
```

### Ejercicio 3: Funciones

**Solución:**
```python
import math

def area_circulo(r):
    return math.pi * r**2

def celsius_fahrenheit(c):
    return (c * 9/5) + 32

def promedio(lista):
    return sum(lista) / len(lista)

def max_min(lista):
    return max(lista), min(lista)
```


### Ejercicio 4: Operaciones con NumPy

**Solución:**
```python
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,4,3,2,1])

suma = arr1 + arr2
multi = arr1 * 2

media = np.mean(arr1)
mediana = np.median(arr1)
std = np.std(arr1)

unicos = np.unique(arr1)

reshape = arr1.reshape(5,1)
```


### Ejercicio 5: Álgebra con NumPy

**Solución:**
```python
import numpy as np

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

punto = np.dot(v1, v2)
cruz = np.cross(v1, v2)

mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)

norm_v1 = v1 / mag_v1
norm_v2 = v2 / mag_v2
```

### Ejercicio 6: DataFrames Básico

**Solución:**
```python
import pandas as pd

data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofia'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

df['nombre']
df[df['promedio'] > 8.5]
df.sort_values(by='edad')

df['aprobado'] = df['promedio'] >= 7

df.groupby('carrera')['promedio'].mean()
```


### Ejercicio 7: Manipulación de Datos

**Solución:**
```python
df.loc[0, 'edad'] = None
df['edad'] = df['edad'].fillna(df['edad'].mean())

df = df.drop_duplicates()

df['promedio_doble'] = df['promedio'].apply(lambda x: x * 2)

df.loc[0]
df.iloc[0]

df2 = df.copy()
df_concat = pd.concat([df, df2])
```


### Ejercicio 8: Matplotlib

**Solución:**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.scatter(x,y)
plt.hist(y)
plt.bar([1,2,3],[3,5,7])

plt.title("Gráficas básicas")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```


### Ejercicio 9: Análisis Exploratorio

**Solución:**
```python
import seaborn as sns

df = sns.load_dataset('iris')

df.info()
df.describe()

df.hist()

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)

sns.boxplot(x='species', y='sepal_length', data=df)
```


### Ejercicio 10: Medidas de Tendencia Central

| Datos | Media | Mediana | Moda |
|------|------|--------|------|
| [5,3,8,3,7] | 5.2 | 5 | 3 |
| [10,20,30,40] | 25 | 25 | No hay |
| [1,2,2,3,3,3,4] | 2.57 | 3 | 3 |


### Ejercicio 11: Dispersión

| Datos | Rango | Varianza | Desv. Estándar |
|------|------|---------|----------------|
| [2,4,4,4,5,5,7,9] | 7 | 4 | 2 |
| [1,3,5,7,9] | 8 | 8 | 2.82 |


### Ejercicio 12: Proceso de Data Science

1. **CRISP-DM:** Metodología que incluye comprensión del negocio, análisis de datos, preparación, modelado, evaluación e implementación.

2. **Fases:**
- Comprensión del problema  
- Análisis de datos  
- Preparación  
- Modelado  
- Evaluación  
- Implementación  

3. **MVP:** Producto mínimo viable que permite validar una solución con el menor esfuerzo posible.


### Ejercicio 13: Caso de Estudio

**Solución:**

Un ejemplo aplicado es el análisis del dataset Titanic.

- **Pregunta:** ¿Qué factores influyen en la supervivencia de los pasajeros?  
- **Técnicas utilizadas:** Análisis exploratorio de datos (EDA), visualización y correlación  
- **Hallazgos:** Variables como el sexo, la clase del pasajero y la edad influyen significativamente en la probabilidad de supervivencia  


## Resumen de Aprendizaje

- Reforcé conceptos básicos de Python
- Practiqué NumPy y Pandas
- Realicé análisis exploratorio de datos
- Comprendí conceptos estadísticos básicos
- Apliqué visualización de datos




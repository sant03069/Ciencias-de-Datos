# |Actividad 3.1: Refuerzo de Python |
# |1. ESTRUCTURAS BÁSICAS            |
# |__________________________________|

# --Lista--
numeros = [10, 20, 30, 40, 50]
print("Lista:", numeros)

# --Diccionario--
persona = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Querétaro"
}
print("Diccionario:", persona)

# --DataFrame--
import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [23, 25, 22],
    "Calificación": [90, 85, 88]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

#_____________________
#|2.FUNCIONES LAMBDA |
#|___________________|

# --Funcion lambda para elevar al cuadrado--
cuadrado = lambda x: x**2
print("\nLambda (cuadrado de 5):", cuadrado(5))

# --Lambda con lista--
numeros_cuadrado = list(map(lambda x: x**2, numeros))
print("Lista con cuadrados:", numeros_cuadrado)

# ________________________
# |3.LIST COMPREHENSIONS |
# |______________________|

# --Crear lista de números pares--
pares = [x for x in range(1, 21) if x % 2 == 0]
print("\nNúmeros pares:", pares)

# --Convertir lista a cuadrados--
cuadrados = [x**2 for x in numeros]
print("Cuadrados con list comprehension:", cuadrados)

#______________________
#|4.MANEJO DE ERRORES |
#|____________________|

try:
    numero = int(input("\nIngresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
except ValueError:
    print("Error: Debes ingresar un número válido.")

#___________________________
#|5. EJERCICIOS BASICOS (5)|
#|_________________________|

# --Ejercicio 1: Suma de una lista--
def suma_lista(lista):
    return sum(lista)

print("\nSuma de la lista:", suma_lista(numeros))

# --Ejercicio 2: Número mayor--
def numero_mayor(lista):
    return max(lista)

print("Número mayor:", numero_mayor(numeros))

# --Ejercicio 3: Contar palabras en una frase--
def contar_palabras(frase):
    return len(frase.split())

print("Cantidad de palabras:", contar_palabras("Hola we esto es python"))

# --Ejercicio 4: Verificar número par o impar--
def es_par(numero):
    return "Par" if numero % 2 == 0 else "Impar"

print("El número 7 es:", es_par(7))

# --Ejercicio 5: Tabla de multiplicar--
def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print("\nTabla del 5:")
tabla_multiplicar(5)
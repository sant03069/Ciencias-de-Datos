# check_libraries.py
import importlib

# Lista de librerías que quieres verificar
librerias = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "tensorflow",
    "torch"
]

print(" Verificando librerías...\n")

for lib in librerias:
    try:
        importlib.import_module(lib)
        print(f"{lib} está instalada y funciona")
    except ImportError:
        print(f"{lib} NO está instalada")
    except Exception as e:
        print(f"⚠️ {lib} tiene un problema: {e}")

print("\nRevisión completa")
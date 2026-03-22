# Reporte Actividad 1

## Importancia de los perfiles de ciencia de datos en DeportivaMX

El crecimiento acelerado de DeportivaMX ha provocado un incremento significativo en la generación de datos, lo que representa un desafío importante para su correcta gestión. Sin una estrategia adecuada, la información puede volverse difícil de organizar y aprovechar, limitando la toma de decisiones. Por ello, es fundamental contar con perfiles especializados en ciencia de datos que permitan transformar los datos en conocimiento útil para el negocio.

El **Data Engineer** tiene la responsabilidad de construir y mantener la infraestructura de datos. Su labor consiste en recolectar información desde diferentes fuentes, procesarla y garantizar que esté disponible de forma confiable. Gracias a este perfil, los datos pueden ser utilizados de manera eficiente por otros equipos.

El **Data Analyst** se enfoca en interpretar los datos y convertirlos en información comprensible. A través de reportes y visualizaciones, identifica tendencias y patrones que ayudan a mejorar procesos como ventas, inventario y estrategias comerciales.

El **Data Scientist** utiliza modelos estadísticos y técnicas avanzadas para analizar grandes volúmenes de datos. Su objetivo es generar predicciones que permitan anticipar comportamientos del mercado y optimizar la toma de decisiones estratégicas.

El **Machine Learning Engineer** se encarga de implementar los modelos desarrollados, asegurando que funcionen correctamente en entornos reales. Además, automatiza procesos para mantener actualizados los sistemas de análisis.

Por último, el **Data Architect** diseña la estructura general de los sistemas de datos, definiendo cómo se almacenan, integran y protegen. Este perfil garantiza que la arquitectura sea escalable, segura y eficiente.

## Las dimensiones del Big Data en DeportivaMX

Para comprender la complejidad del manejo de datos, se analizan las 5 V del Big Data:

### Volumen
Se refiere a la gran cantidad de datos generados por la empresa. En DeportivaMX, este volumen incluye registros de ventas, información de clientes, productos y actividad en línea. A medida que la empresa crece, también lo hace la cantidad de datos, lo que requiere sistemas de almacenamiento robustos y escalables como Data Lakes o bases distribuidas.

### Velocidad
La velocidad indica la rapidez con la que los datos se generan y deben ser procesados. En un entorno de comercio electrónico como DeportivaMX, las transacciones ocurren en tiempo real, por lo que es necesario procesar la información de manera inmediata para tomar decisiones rápidas, como ajustar precios, gestionar inventarios o detectar fraudes.

### Variedad
Hace referencia a los distintos tipos de datos que maneja la empresa. Estos pueden ser:
- Datos estructurados (bases de datos tradicionales)
- Datos semiestructurados (archivos JSON o XML)
- Datos no estructurados (comentarios, imágenes, redes sociales)

### Veracidad
La veracidad se relaciona con la calidad y confiabilidad de los datos. Datos incorrectos, incompletos o duplicados pueden generar decisiones equivocadas. Por ello, es importante implementar procesos de limpieza, validación y control de calidad que aseguren la precisión de la información.

### Valor
El valor es el objetivo principal del Big Data: transformar los datos en beneficios para la empresa. En DeportivaMX, esto puede traducirse en:
- Mejor conocimiento del cliente
- Optimización de inventarios
- Personalización de ofertas
- Incremento en ventas
  
## Propuesta de arquitectura de datos

Para hacer frente al crecimiento de DeportivaMX, se propone una arquitectura basada en un **Data Lake**, que permite almacenar grandes volúmenes de datos en su formato original.

### Beneficios principales:

- Permite almacenar datos estructurados, semiestructurados y no estructurados  
- Es altamente escalable conforme crece la empresa  
- Facilita el análisis avanzado y el uso de inteligencia artificial  
- Reduce costos al evitar transformaciones iniciales innecesarias  

## Proceso de manejo de datos

El flujo de datos dentro de la empresa puede organizarse en las siguientes etapas:

1. **Captura de datos:**  
   Se recopila información de distintas fuentes como ventas, clientes y productos.

2. **Almacenamiento:**  
   Los datos se guardan en el Data Lake sin modificar su estructura original.

3. **Preparación:**  
   Se realiza limpieza y transformación de los datos para su análisis.

4. **Análisis:**  
   Se obtienen insights y se desarrollan modelos predictivos.

5. **Visualización:**  
   Se presentan los resultados mediante dashboards que facilitan la toma de decisiones.

## Coleccion de Datos

### Análisis de la Base de Datos NoSQL

Se diseñaron 4 colecciones principales:

- **Usuarios**: información personal y preferencias  
- **Productos**: datos del catálogo e inventario  
- **Órdenes**: registro de compras realizadas  
- **Reseñas**: opiniones de los clientes  

La base de datos utiliza un modelo **NoSQL flexible**, lo que permite:
- Agregar nuevos campos sin afectar la estructura  
- Manejar grandes volúmenes de datos  
- Relacionar información mediante identificadores (IDs)  

También se usan datos semiestructurados como:
- Arreglos (listas de productos o compras)  
- Objetos anidados (dirección, inventario, detalles)  

Este diseño facilita:
- Escalabilidad  
- Integración con aplicaciones  
- Análisis del comportamiento del cliente

```
[
{
  "_id": "USR1001",
  "nombre_completo": "Carlos Ramírez",
  "email": "carlos.ramirez@email.com",
  "telefono": "4427654321",
  "ubicacion": {
    "ciudad": "Querétaro",
    "pais": "México"
  },
  "preferencias": {
    "categorias_favoritas": ["Ropa deportiva", "Accesorios"],
    "metodo_pago_preferido": "Tarjeta"
  },
  "compras_realizadas": ["ORD5001", "ORD5002"]
},

{
  "_id": "PRD2001",
  "nombre_producto": "Playera deportiva",
  "marca": "Adidas",
  "precio": 599.99,
  "inventario": {
    "disponibles": 120,
    "almacen": "QRO-01"
  },
  "detalles": {
    "color": "Negro",
    "tallas": ["S", "M", "L", "XL"]
  },
  "categoria": "Ropa"
},

{
  "_id": "ORD5001",
  "usuario_id": "USR1001",
  "fecha_compra": "2026-03-20",
  "productos": [
    {
      "producto_id": "PRD2001",
      "cantidad": 2,
      "precio_unitario": 599.99
    }
  ],
  "total": 1199.98,
  "estado": "Entregado"
},

{
  "_id": "REV3001",
  "producto_id": "PRD2001",
  "usuario_id": "USR1001",
  "calificacion": 5,
  "comentario": "Muy buena calidad y cómoda para entrenar",
  "fecha": "2026-03-21"
}
]

```


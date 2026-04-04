# Actividad2.4
## JUSTIFICACIÓN

Se diseñó un modelo de datos basado en MongoDB utilizando colecciones independientes para representar entidades principales como libros, usuarios, préstamos, autores y categorías.

Se optó por utilizar referencias mediante identificadores (ObjectId) para relacionar los documentos, lo que permite mantener la flexibilidad del modelo NoSQL y evitar redundancia de datos.

Este diseño facilita la escalabilidad del sistema, permitiendo agregar nuevos documentos sin afectar la estructura existente, lo cual es una ventaja clave de las bases de datos NoSQL frente a modelos relacionales tradicionales.

```json
{
  "libros": [
    {
      "_id": "ObjectId",
      "titulo": "El principito",
      "autor_id": "ObjectId",
      "categoria_id": "ObjectId",
      "anio": 1943,
      "disponible": true
    }
  ],
  "usuarios": [
    {
      "_id": "ObjectId",
      "nombre": "Juan Pérez",
      "email": "juan@email.com",
      "telefono": "4421234567"
    }
  ],
  "prestamos": [
    {
      "_id": "ObjectId",
      "usuario_id": "ObjectId",
      "libro_id": "ObjectId",
      "fecha_prestamo": "2026-04-03",
      "fecha_devolucion": "2026-04-10"
    }
  ],
  "autores": [
    {
      "_id": "ObjectId",
      "nombre": "Gabriel García Márquez",
      "nacionalidad": "Colombiana"
    }
  ],
  "categorias": [
    {
      "_id": "ObjectId",
      "nombre": "Ficción"
    }
  ]
}
```


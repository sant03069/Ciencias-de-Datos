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

### Ejercicio 2: 

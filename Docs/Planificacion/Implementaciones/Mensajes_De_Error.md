# Mensajes de Error y Advertencia - Calculadora de Matrices

Este documento recopila los mensajes de error y advertencia que puede arrojar la Calculadora de Matrices, junto con su significado y posibles soluciones para el usuario.

---

## Errores de Validación de Entradas
- **Error: Las matrices deben tener el mismo tamaño para la suma/resta.**
  - Solución: Verifica que ambas matrices tengan igual número de filas y columnas.
- **Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda para multiplicar.**
  - Solución: Ajusta las dimensiones de las matrices.
- **Error: La matriz debe ser cuadrada.**
  - Solución: Ingresa una matriz con igual número de filas y columnas.
- **Error: Todos los valores deben ser números reales.**
  - Solución: Revisa que no haya celdas vacías o caracteres no numéricos.

## Errores de Operación
- **Error: Matriz singular, no tiene inversa.**
  - Solución: Verifica que el determinante no sea cero.
- **Error: Sistema incompatible o indeterminado.**
  - Solución: Revisa los datos del sistema de ecuaciones.
- **Error: División por cero detectada.**
  - Solución: Revisa los valores de la matriz y evita ceros en posiciones críticas.

## Errores de Backend/API
- **Error: No se pudo conectar con el servidor.**
  - Solución: Verifica que el backend esté en ejecución.
- **Error: Formato de datos inválido.**
  - Solución: Revisa la estructura de los datos enviados.

---

Todos los mensajes deben ser claros, en español y orientados al usuario final. Ante dudas, consulta la documentación o solicita ayuda al docente.

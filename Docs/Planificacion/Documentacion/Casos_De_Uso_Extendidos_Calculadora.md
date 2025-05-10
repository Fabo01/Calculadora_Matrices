# Casos de Uso Extendidos - Calculadora de Matrices

Este documento presenta la descripción extendida y detallada de los casos de uso para la Calculadora de Matrices.

## Índice de Casos de Uso Extendidos

1. [Sumar Matrices](#cu-01-sumar-matrices)
2. [Restar Matrices](#cu-02-restar-matrices)
3. [Multiplicar Matrices](#cu-03-multiplicar-matrices)
4. [Calcular Determinante](#cu-04-calcular-determinante)
5. [Calcular Inversa](#cu-05-calcular-inversa)
6. [Resolver Sistema de Ecuaciones](#cu-06-resolver-sistema-de-ecuaciones)
7. [Visualizar Pasos Intermedios](#cu-07-visualizar-pasos-intermedios)
8. [Validar Entradas](#cu-08-validar-entradas)
9. [Manejar Errores](#cu-09-manejar-errores)
10. [Consultar Teoría y Ejemplos](#cu-10-consultar-teoría-y-ejemplos)
11. [Guardar y Consultar Historial](#cu-11-guardar-y-consultar-historial)

---

# Gestión de Operaciones Matriciales

## CU-01: Sumar Matrices

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario ingresa dos matrices de igual tamaño (n x m, n,m ≤ 4).
- El sistema valida que ambas matrices tengan dimensiones compatibles y que todos los datos sean numéricos.
- Si la validación es exitosa, el sistema realiza la suma elemento a elemento, registrando cada operación (por ejemplo, "A[1,1] + B[1,1] = C[1,1]").
- Se muestran los pasos intermedios y el resultado final.

**Flujos Alternativos y Validaciones:**
- Si las dimensiones no coinciden, se muestra un mensaje de error: "Error: Las matrices deben tener el mismo tamaño para la suma."
- Si algún dato no es numérico, se muestra: "Error: Todos los valores deben ser números reales."

**Postcondiciones:**
- Se muestra la matriz resultado y el detalle de la suma por elemento.

---

## CU-02: Restar Matrices

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario ingresa dos matrices de igual tamaño.
- El sistema valida dimensiones y datos numéricos.
- Si la validación es exitosa, el sistema realiza la resta elemento a elemento, registrando cada operación.
- Se muestran los pasos intermedios y el resultado final.

**Flujos Alternativos y Validaciones:**
- Dimensiones incompatibles: mensaje de error.
- Datos no numéricos: mensaje de error.

**Postcondiciones:**
- Se muestra la matriz resultado y el detalle de la resta.

---

## CU-03: Multiplicar Matrices

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario ingresa dos matrices.
- El sistema valida que el número de columnas de la primera matriz sea igual al número de filas de la segunda y que los datos sean numéricos.
- Si la validación es exitosa, el sistema realiza la multiplicación fila por columna, registrando cada operación (por ejemplo, "A[1,:] x B[:,1] = C[1,1]").
- Se muestran los pasos intermedios y el resultado final.

**Flujos Alternativos y Validaciones:**
- Dimensiones incompatibles: mensaje de error.
- Datos no numéricos: mensaje de error.

**Postcondiciones:**
- Se muestra la matriz resultado y el detalle del cálculo de cada elemento.

---

## CU-04: Calcular Determinante

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario ingresa una matriz cuadrada.
- El sistema valida la cuadratura y los datos numéricos.
- Si la validación es exitosa, el sistema calcula el determinante mostrando los pasos (expansión por cofactores, reducción, etc.).
- Se muestran los pasos intermedios y el resultado final.

**Flujos Alternativos y Validaciones:**
- Matriz no cuadrada: mensaje de error.
- Datos no numéricos: mensaje de error.

**Postcondiciones:**
- Se muestra el valor del determinante y el procedimiento seguido.

---

## CU-05: Calcular Inversa

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario ingresa una matriz cuadrada.
- El sistema valida la cuadratura, la no singularidad y los datos numéricos.
- Si la validación es exitosa, el sistema calcula la inversa mostrando los pasos (matriz aumentada, operaciones elementales, etc.).
- Se muestran los pasos intermedios y el resultado final.

**Flujos Alternativos y Validaciones:**
- Matriz singular: mensaje de error.
- Matriz no cuadrada: mensaje de error.
- Datos no numéricos: mensaje de error.

**Postcondiciones:**
- Se muestra la matriz inversa y el procedimiento seguido.

---

# Resolución de Sistemas de Ecuaciones

## CU-06: Resolver Sistema de Ecuaciones (Gauss, Gauss-Jordan, LU)

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario ingresa la matriz de coeficientes y el vector de términos independientes.
- El sistema valida dimensiones, cuadratura y datos numéricos.
- El usuario selecciona el método de resolución (Gauss, Gauss-Jordan, LU).
- El sistema ejecuta el método seleccionado, registrando cada operación elemental, matriz intermedia y sustitución.
- Se muestran los pasos intermedios y la solución final.

**Flujos Alternativos y Validaciones:**
- Sistema incompatible o indeterminado: mensaje de advertencia.
- Datos no numéricos: mensaje de error.

**Postcondiciones:**
- Se muestra la solución del sistema y el detalle del procedimiento.

---

# Visualización y Validaciones

## CU-07: Visualizar Pasos Intermedios

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario puede solicitar ver el desarrollo paso a paso de cualquier operación realizada.
- El sistema muestra la lista de pasos y matrices intermedias, permitiendo al usuario navegar entre ellos.

**Postcondiciones:**
- El usuario comprende el procedimiento seguido.

---

## CU-08: Validar Entradas

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El sistema valida automáticamente las dimensiones y los datos ingresados antes de ejecutar cualquier operación.
- Si hay errores, muestra mensajes claros y orientados al usuario.

**Postcondiciones:**
- Solo se permite ejecutar operaciones con datos válidos.

---

## CU-09: Manejar Errores

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El sistema detecta y reporta errores numéricos o de entrada, mostrando mensajes claros en español.
- Los mensajes de error son específicos según el tipo de error (dimensiones, tipo de datos, singularidad, etc.).

**Postcondiciones:**
- El usuario comprende el motivo del error y puede corregirlo.

---

## CU-10: Consultar Teoría y Ejemplos

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario puede consultar la teoría y ejemplos de los métodos algebraicos implementados.
- El sistema muestra la información teórica y ejemplos numéricos detallados.

**Postcondiciones:**
- El usuario comprende el fundamento teórico y el procedimiento.

---

## CU-11: Guardar y Consultar Historial (Opcional)

**Actores:** Usuario (Estudiante/Docente)

**Descripción Extendida:**
- El usuario puede guardar el historial de operaciones y consultar resultados anteriores.
- El sistema almacena y recupera las operaciones y resultados bajo demanda.

**Postcondiciones:**
- El usuario puede revisar operaciones pasadas.

---

Este documento debe complementarse con diagramas de casos de uso y diagramas de secuencia para cada operación principal.

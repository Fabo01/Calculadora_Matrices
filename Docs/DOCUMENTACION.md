# Documentación de la Calculadora de Matrices

## Índice
1. [Introducción](#introducción)
2. [Requerimientos](#requerimientos)
   - [Funcionales](#requerimientos-funcionales)
   - [No funcionales](#requerimientos-no-funcionales)
3. [Arquitectura y Patrones de Diseño](#arquitectura-y-patrones-de-diseño)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Descripción de Módulos y Clases](#descripción-de-módulos-y-clases)
6. [Validaciones y Manejo de Errores](#validaciones-y-manejo-de-errores)
7. [Explicación de Métodos Algebraicos](#explicación-de-métodos-algebraicos)
8. [Interfaz de Usuario (React.js)](#interfaz-de-usuario-reactjs)
9. [Referencias](#referencias)

---

## Introducción
La Calculadora de Matrices es una herramienta desarrollada en Python (backend) y React.js (frontend) que permite realizar operaciones matriciales básicas (suma, resta, multiplicación, determinante, inversa) y resolver sistemas de ecuaciones lineales utilizando los métodos de Gauss, Gauss-Jordan y factorización LU. El sistema está diseñado para matrices de hasta 4x4, mostrando paso a paso el desarrollo algebraico y validando errores numéricos y de entrada.

Esta calculadora está orientada a la docencia y la práctica de álgebra lineal, permitiendo a los usuarios comprender el proceso detrás de cada operación, visualizar los pasos intermedios y detectar errores comunes en la manipulación de matrices.

## Requerimientos
### Requerimientos Funcionales
- Sumar, restar y multiplicar matrices de hasta 4x4.
- Calcular determinantes e inversas de matrices cuadradas (hasta 4x4).
- Resolver sistemas de ecuaciones lineales por:
  - Eliminación Gaussiana
  - Gauss-Jordan
  - Factorización LU
- Mostrar paso a paso cada operación realizada, incluyendo las matrices intermedias y las operaciones elementales.
- Validar dimensiones y entradas de matrices (solo números reales, sin valores vacíos, dimensiones correctas).
- Analizar y reportar errores numéricos (singularidad, división por cero, matrices no invertibles, etc).
- Documentar y explicar los métodos algebraicos implementados, mostrando la teoría y el procedimiento seguido.

#### Ejemplo de uso funcional:
- El usuario ingresa dos matrices 3x3 y selecciona "Multiplicación". El sistema valida dimensiones, realiza la operación, muestra cada paso (producto fila por columna), y entrega el resultado final junto con los pasos intermedios.

### Requerimientos No Funcionales
- No utilizar librerías externas para operaciones matriciales (todo el cálculo debe ser implementado manualmente).
- Código siguiendo principios SOLID y patrones de diseño para facilitar la mantenibilidad y extensibilidad.
- Arquitectura desacoplada y mantenible (Clean Architecture), permitiendo separar lógica, presentación y adaptadores.
- Nombres de variables y métodos en snake_case y en español para facilitar la comprensión y estandarización.
- Interfaz de usuario intuitiva, clara y completamente en español.
- Mensajes de error claros, detallados y orientados al usuario final.
- Documentación exhaustiva y ejemplos de uso.

## Arquitectura y Patrones de Diseño

### Arquitectura Limpia (Clean Architecture)
- **Capas:**
  - **Dominio:** Entidades, lógica de negocio y contratos (interfaces).
  - **Aplicación:** Casos de uso, orquestación de operaciones y lógica de aplicación.
  - **Infraestructura:** Adaptadores para entrada/salida, persistencia, servicios externos.
  - **Presentación:** API REST (por ejemplo, FastAPI o Flask) que expone los servicios al frontend.
- **Ventajas:**
  - Alta mantenibilidad y testabilidad.
  - Fácil de extender con nuevas operaciones o métodos.
  - Independencia de frameworks y tecnologías externas.

### Patrones de Diseño
- **Command:** Cada operación matricial (suma, resta, multiplicación, determinante, inversa, resolución de sistemas) se implementa como un comando, encapsulando la lógica y el registro de pasos.
- **Strategy:** Permite seleccionar dinámicamente el método algebraico (Gauss, Gauss-Jordan, LU) para la resolución de sistemas.
- **Factory:** Facilita la creación de matrices y operaciones según el tipo y dimensiones requeridas.
- **Validador y Excepciones Personalizadas:** Robustez y claridad en el manejo de errores, desacoplando la validación de la lógica de negocio.

#### Diagrama sugerido:
- Incluir un diagrama de capas y un diagrama de clases que muestre la relación entre `Matriz`, `OperacionMatriz`, `MetodoResolucion`, y los comandos.

## Estructura del Proyecto
```
Backend/
  Aplicacion/
    calculadora_matrices.py
    validador.py
  Dominio/
    matriz.py
    operacion_matriz.py
    metodo_resolucion.py
    excepciones.py
  Infraestructura/
    adaptador_api.py
    persistencia.py (opcional)
  Presentacion/
    api.py
Docs/
  DOCUMENTACION.md
  informe.tex
  Pauta Calculadora Matrices.pdf
Frontend/
  src/
    components/
    pages/
    utils/
```

## Descripción de Módulos y Clases

### Dominio
- **`matriz.py`**
  - `class Matriz`:
    - Representa una matriz de hasta 4x4.
    - Métodos: `es_cuadrada()`, `copiar()`, `mostrar()`, `validar_dimensiones()`, etc.
    - Atributos: `filas`, `columnas`, `datos` (lista de listas).
    - Validaciones: dimensiones, tipo de datos, rango permitido.

- **`operacion_matriz.py`**
  - `class OperacionMatriz` (abstracta):
    - Método abstracto: `ejecutar(matriz_a, matriz_b=None)`.
    - Registra los pasos realizados en la operación.
  - Subclases:
    - `SumaMatriz`, `RestaMatriz`, `MultiplicacionMatriz`, `DeterminanteMatriz`, `InversaMatriz`.
    - Cada una implementa `ejecutar` y registra los pasos intermedios.

- **`metodo_resolucion.py`**
  - `class MetodoResolucion` (abstracta):
    - Método abstracto: `resolver(matriz_aumentada)`.
    - Registra los pasos de resolución.
  - Subclases:
    - `Gauss`, `GaussJordan`, `LU`.
    - Cada una implementa el algoritmo correspondiente y registra los pasos.

- **`excepciones.py`**
  - Excepciones personalizadas:
    - `DimensionInvalidaError`, `MatrizSingularError`, `OperacionNoSoportadaError`, `EntradaInvalidaError`.
    - Cada excepción incluye un mensaje descriptivo en español.

### Aplicacion
- **`calculadora_matrices.py`**
  - Orquesta la ejecución de operaciones y métodos de resolución.
  - Recibe las matrices y la operación/método a ejecutar.
  - Devuelve el resultado y los pasos realizados.

- **`validador.py`**
  - Funciones para validar dimensiones, tipo de datos, cuadratura, etc.
  - Lanza excepciones personalizadas en caso de error.

### Infraestructura
- **`adaptador_api.py`**
  - Traduce las solicitudes del frontend a llamadas a la lógica de aplicación.
  - Formatea las respuestas y los mensajes de error.
- **`persistencia.py`** (opcional)
  - Permite guardar el historial de operaciones y resultados.

### Presentacion
- **`api.py`**
  - Implementa la API REST (por ejemplo, con FastAPI o Flask).
  - Expone endpoints para cada operación y método de resolución.
  - Documenta los endpoints y los parámetros esperados.

## Validaciones y Manejo de Errores

### Validaciones
- **Dimensiones:**
  - Suma y resta: matrices de igual tamaño.
  - Multiplicación: columnas de la primera igual a filas de la segunda.
  - Determinante/inversa: matriz cuadrada.
  - Métodos de resolución: matriz aumentada de tamaño n x (n+1).
- **Tipo de datos:**
  - Solo números reales (float/int).
  - No se permiten valores vacíos o nulos.
- **Rango:**
  - Máximo 4x4.

### Manejo de Errores
- **Excepciones personalizadas:**
  - `DimensionInvalidaError`: dimensiones incompatibles.
  - `MatrizSingularError`: matriz no invertible o determinante cero.
  - `OperacionNoSoportadaError`: operación no implementada.
  - `EntradaInvalidaError`: datos no numéricos o fuera de rango.
- **Mensajes de error:**
  - Siempre en español, claros y orientados al usuario.
  - Ejemplo: "Error: Las matrices deben tener el mismo tamaño para la suma."

### Ejemplo de uso de excepciones:
```python
try:
    resultado, pasos = SumaMatriz().ejecutar(matriz_a, matriz_b)
except DimensionInvalidaError as e:
    print(f"Error: {e}")
```

## Explicación de Métodos Algebraicos

### Eliminación Gaussiana
- **Descripción:**
  - Transforma la matriz aumentada del sistema en una matriz triangular superior mediante operaciones elementales por filas.
  - Permite resolver el sistema por sustitución regresiva.
- **Pasos detallados:**
  1. Formar la matriz aumentada `[A|B]`.
  2. Anular los coeficientes por debajo de la diagonal principal usando operaciones elementales.
  3. Registrar cada operación (por ejemplo, "F2 - 2*F1 → F2").
  4. Resolver por sustitución regresiva, mostrando cada paso.
- **Ejemplo:**
  - Ver ejemplos numéricos en el informe.

### Gauss-Jordan
- **Descripción:**
  - Lleva la matriz aumentada a la forma escalonada reducida (identidad) usando operaciones elementales por filas.
  - Permite obtener la solución directamente, sin sustitución regresiva.
- **Pasos detallados:**
  1. Formar la matriz aumentada `[A|B]`.
  2. Anular todos los elementos de cada columna excepto el pivote.
  3. Registrar cada operación y matriz intermedia.
  4. La solución se obtiene directamente de la última columna.
- **Ejemplo:**
  - Ver ejemplos numéricos en el informe.

### Factorización LU
- **Descripción:**
  - Descompone la matriz A en el producto de una matriz triangular inferior (L) y una superior (U).
  - Permite resolver varios sistemas con la misma matriz de coeficientes.
- **Pasos detallados:**
  1. Factorizar A en L y U (por ejemplo, método de Doolittle).
  2. Resolver LY = B por sustitución progresiva.
  3. Resolver UX = Y por sustitución regresiva.
  4. Registrar cada paso de factorización y sustitución.
- **Ejemplo:**
  - Ver ejemplos numéricos en el informe.

## Interfaz de Usuario (React.js)

### Requisitos de la Interfaz
- Formulario para ingresar matrices (inputs dinámicos para hasta 4x4).
- Selección de operación (suma, resta, multiplicación, determinante, inversa, método de resolución).
- Botón para ejecutar la operación.
- Visualización de matrices de entrada y resultado en formato tabular.
- Visualización paso a paso de cada operación realizada (lista de pasos, matrices intermedias).
- Mensajes de error claros y en español.
- Validación de entradas antes de enviar al backend (dimensiones, tipo de datos, rango).

### Sugerencia de Componentes
- `MatrizInput`: Componente para ingresar los valores de la matriz.
- `OperacionSelector`: Selector de operación/método.
- `PasosOperacion`: Muestra los pasos realizados y matrices intermedias.
- `ResultadoMatriz`: Muestra el resultado final.
- `ErrorMensaje`: Muestra mensajes de error.

### Flujo de la Interfaz
1. El usuario ingresa las matrices y selecciona la operación.
2. El frontend valida las entradas y envía la solicitud al backend.
3. El backend responde con el resultado y los pasos.
4. El frontend muestra el resultado y los pasos de forma clara y visual.

### Ejemplo de respuesta esperada del backend
```json
{
  "resultado": [[1,2],[3,4]],
  "pasos": [
    "F2 - 2*F1 → F2",
    "F1: [1, 2]",
    "F2: [0, 1]"
  ]
}
```

## Referencias
- Informe y pauta del proyecto.
- Bibliografía de álgebra lineal y métodos numéricos (ver sección de referencias en `informe.tex`).
- Ejemplos y procedimientos extraídos de la pauta y el informe.

---

Esta documentación debe ser complementada con diagramas de clases, diagramas de flujo de operaciones y ejemplos de uso en los archivos correspondientes del proyecto.

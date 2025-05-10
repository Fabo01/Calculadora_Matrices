# Diagramas UML y de Arquitectura - Calculadora de Matrices

Este documento presenta los diagramas UML y de arquitectura para la Calculadora de Matrices.

## Índice
1. [Diagrama de Arquitectura](#diagrama-de-arquitectura)
2. [Diagrama de Patrones de Diseño](#diagrama-de-patrones-de-diseño)
3. [Diagrama de Clases](#diagrama-de-clases)
4. [Modelo Entidad-Relación](#modelo-entidad-relación)
5. [Diagrama de Objetos](#diagrama-de-objetos)
6. [Diagrama de Componentes](#diagrama-de-componentes)

---

## Diagrama de Arquitectura

```mermaid
flowchart TD
    subgraph "Frontend (React)"
        UI[Componentes UI]
        SVC[Servicios API]
    end
    subgraph "Backend (Python)"
        API[API REST]
        APP[Aplicación]
        DOM[Dominio]
        INF[Infraestructura]
    end
    UI <--> SVC
    SVC <--> API
    API <--> APP
    APP <--> DOM
    APP <--> INF
    INF <--> DOM
    DB[(Historial de Operaciones)]
    INF <--> DB
    classDef frontend fill:#d0e0ff,stroke:#3c78d8,stroke-width:1px
    classDef backend fill:#f9f9f9,stroke:#999,stroke-width:1px
    class UI,SVC frontend
    class API,APP,DOM,INF backend
```

---

## Diagrama de Patrones de Diseño

```mermaid
classDiagram
    class OperacionMatriz {
        +ejecutar(matriz_a, matriz_b)
        +pasos: list
    }
    class SumaMatriz
    class RestaMatriz
    class MultiplicacionMatriz
    class DeterminanteMatriz
    class InversaMatriz
    OperacionMatriz <|-- SumaMatriz
    OperacionMatriz <|-- RestaMatriz
    OperacionMatriz <|-- MultiplicacionMatriz
    OperacionMatriz <|-- DeterminanteMatriz
    OperacionMatriz <|-- InversaMatriz
    class MetodoResolucion {
        +resolver(matriz_aumentada)
        +pasos: list
    }
    class Gauss
    class GaussJordan
    class LU
    MetodoResolucion <|-- Gauss
    MetodoResolucion <|-- GaussJordan
    MetodoResolucion <|-- LU
    class Validador
    class ExcepcionPersonalizada
    class CalculadoraMatrices
    CalculadoraMatrices --> OperacionMatriz
    CalculadoraMatrices --> MetodoResolucion
    CalculadoraMatrices --> Validador
    Validador --> ExcepcionPersonalizada
```

---

## Diagrama de Clases

```mermaid
classDiagram
    class Matriz {
        -filas: int
        -columnas: int
        -datos: list
        +es_cuadrada()
        +copiar()
        +mostrar()
        +validar_dimensiones()
    }
    class OperacionMatriz {
        +ejecutar(matriz_a, matriz_b)
        +pasos: list
    }
    class MetodoResolucion {
        +resolver(matriz_aumentada)
        +pasos: list
    }
    class SumaMatriz
    class RestaMatriz
    class MultiplicacionMatriz
    class DeterminanteMatriz
    class InversaMatriz
    class Gauss
    class GaussJordan
    class LU
    Matriz --> OperacionMatriz
    OperacionMatriz <|-- SumaMatriz
    OperacionMatriz <|-- RestaMatriz
    OperacionMatriz <|-- MultiplicacionMatriz
    OperacionMatriz <|-- DeterminanteMatriz
    OperacionMatriz <|-- InversaMatriz
    MetodoResolucion <|-- Gauss
    MetodoResolucion <|-- GaussJordan
    MetodoResolucion <|-- LU
```

---

## Modelo Entidad-Relación (MER)

```mermaid
erDiagram
    MATRIZ ||--o{ OPERACION : utiliza
    OPERACION ||--o{ PASO : registra
    MATRIZ ||--o{ METODO_RESOLUCION : resuelve
    METODO_RESOLUCION ||--o{ PASO : registra
```

---

## Diagrama de Objetos

```mermaid
classDiagram
    class Matriz_A {
        datos = [[1,2],[3,4]]
    }
    class Matriz_B {
        datos = [[5,6],[7,8]]
    }
    class SumaMatriz
    Matriz_A --> SumaMatriz
    Matriz_B --> SumaMatriz
    SumaMatriz --> Matriz_Resultado
    class Matriz_Resultado {
        datos = [[6,8],[10,12]]
    }
```

---

## Diagrama de Componentes

```mermaid
flowchart TD
    Frontend -->|API REST| Backend
    Backend -->|Lógica| Dominio
    Backend -->|Validación| Validador
    Backend -->|Persistencia| Historial
    Dominio -->|Excepciones| Excepciones
```

---

Estos diagramas deben complementarse con los diagramas de secuencia y casos de uso para una documentación completa.

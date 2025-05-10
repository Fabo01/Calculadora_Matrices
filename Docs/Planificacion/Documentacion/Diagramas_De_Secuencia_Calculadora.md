# Diagramas de Secuencia - Calculadora de Matrices

Este documento presenta los diagramas de secuencia para todos los casos de uso principales y extendidos de la Calculadora de Matrices.

---

## CU-01: Sumar Matrices

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matrices y selecciona "Suma"
    UI->>API: POST /sumar_matrices
    API->>APP: Ejecutar suma
    APP->>DOM: Validar dimensiones y datos
    DOM-->>APP: OK
    APP->>DOM: Sumar matrices
    DOM-->>APP: Resultado y pasos
    APP-->>API: Resultado y pasos
    API-->>UI: Resultado y pasos
    UI-->>Usuario: Muestra resultado y pasos
```

---

## CU-02: Restar Matrices

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matrices y selecciona "Resta"
    UI->>API: POST /restar_matrices
    API->>APP: Ejecutar resta
    APP->>DOM: Validar dimensiones y datos
    DOM-->>APP: OK
    APP->>DOM: Restar matrices
    DOM-->>APP: Resultado y pasos
    APP-->>API: Resultado y pasos
    API-->>UI: Resultado y pasos
    UI-->>Usuario: Muestra resultado y pasos
```

---

## CU-03: Multiplicar Matrices

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matrices y selecciona "Multiplicación"
    UI->>API: POST /multiplicar_matrices
    API->>APP: Ejecutar multiplicación
    APP->>DOM: Validar dimensiones y datos
    DOM-->>APP: OK
    APP->>DOM: Multiplicar matrices
    DOM-->>APP: Resultado y pasos
    APP-->>API: Resultado y pasos
    API-->>UI: Resultado y pasos
    UI-->>Usuario: Muestra resultado y pasos
```

---

## CU-04: Calcular Determinante

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matriz y selecciona "Determinante"
    UI->>API: POST /calcular_determinante
    API->>APP: Ejecutar determinante
    APP->>DOM: Validar cuadratura y datos
    DOM-->>APP: OK
    APP->>DOM: Calcular determinante
    DOM-->>APP: Resultado y pasos
    APP-->>API: Resultado y pasos
    API-->>UI: Resultado y pasos
    UI-->>Usuario: Muestra resultado y pasos
```

---

## CU-05: Calcular Inversa

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matriz y selecciona "Inversa"
    UI->>API: POST /calcular_inversa
    API->>APP: Ejecutar inversa
    APP->>DOM: Validar cuadratura, singularidad y datos
    DOM-->>APP: OK
    APP->>DOM: Calcular inversa
    DOM-->>APP: Resultado y pasos
    APP-->>API: Resultado y pasos
    API-->>UI: Resultado y pasos
    UI-->>Usuario: Muestra resultado y pasos
```

---

## CU-06: Resolver Sistema de Ecuaciones

### CU-06a: Eliminación Gaussiana

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matriz aumentada y selecciona "Gauss"
    UI->>API: POST /resolver_sistema_gauss
    API->>APP: Ejecutar método Gauss
    APP->>DOM: Validar dimensiones y datos
    DOM-->>APP: OK
    APP->>DOM: Ejecutar Gauss
    DOM-->>APP: Solución y pasos
    APP-->>API: Solución y pasos
    API-->>UI: Solución y pasos
    UI-->>Usuario: Muestra solución y pasos
```

---

### CU-06b: Gauss-Jordan

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matriz aumentada y selecciona "Gauss-Jordan"
    UI->>API: POST /resolver_sistema_gauss_jordan
    API->>APP: Ejecutar método Gauss-Jordan
    APP->>DOM: Validar dimensiones y datos
    DOM-->>APP: OK
    APP->>DOM: Ejecutar Gauss-Jordan
    DOM-->>APP: Solución y pasos
    APP-->>API: Solución y pasos
    API-->>UI: Solución y pasos
    UI-->>Usuario: Muestra solución y pasos
```

---

### CU-06c: Factorización LU

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    participant DOM as Dominio
    Usuario->>UI: Ingresa matriz aumentada y selecciona "LU"
    UI->>API: POST /resolver_sistema_lu
    API->>APP: Ejecutar método LU
    APP->>DOM: Validar dimensiones y datos
    DOM-->>APP: OK
    APP->>DOM: Ejecutar LU
    DOM-->>APP: Solución y pasos
    APP-->>API: Solución y pasos
    API-->>UI: Solución y pasos
    UI-->>Usuario: Muestra solución y pasos
```

---

## CU-07: Visualizar Pasos Intermedios

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    Usuario->>UI: Solicita ver pasos intermedios
    UI->>API: GET /obtener_pasos
    API->>APP: Obtener pasos de la operación
    APP-->>API: Pasos intermedios
    API-->>UI: Pasos intermedios
    UI-->>Usuario: Muestra pasos y matrices intermedias
```

---

## CU-08: Validar Entradas

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    Usuario->>UI: Ingresa datos en formularios
    UI->>API: POST /validar_entradas
    API->>APP: Validar dimensiones y datos
    APP-->>API: OK/Error
    API-->>UI: Mensaje de validación
    UI-->>Usuario: Muestra mensaje de validación
```

---

## CU-09: Manejar Errores

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    Usuario->>UI: Intenta ejecutar operación
    UI->>API: POST /ejecutar_operacion
    API->>APP: Ejecutar operación
    APP-->>API: Error detectado
    API-->>UI: Mensaje de error
    UI-->>Usuario: Muestra mensaje de error
```

---

## CU-10: Consultar Teoría y Ejemplos

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    Usuario->>UI: Solicita teoría o ejemplo
    UI->>API: GET /teoria_o_ejemplo
    API-->>UI: Muestra teoría o ejemplo
    UI-->>Usuario: Visualiza teoría o ejemplo
```

---

## CU-11: Guardar y Consultar Historial (Opcional)

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Interfaz de Usuario (React)
    participant API as API REST
    participant APP as Aplicación
    Usuario->>UI: Solicita guardar/consultar historial
    UI->>API: POST /historial
    API->>APP: Guardar/consultar historial
    APP-->>API: Historial
    API-->>UI: Historial
    UI-->>Usuario: Muestra historial
```

---

Estos diagramas deben complementarse con los diagramas de clases y arquitectura para una documentación completa.

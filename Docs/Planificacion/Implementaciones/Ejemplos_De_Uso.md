# Ejemplos de Uso - Calculadora de Matrices

Este documento presenta ejemplos numéricos completos para cada operación principal de la Calculadora de Matrices, incluyendo entradas, salidas esperadas y pasos intermedios.

---

## Suma de Matrices

**Entrada:**
- Matriz A:
  | 1 | 2 |
  |---|---|
  | 3 | 4 |
- Matriz B:
  | 5 | 6 |
  |---|---|
  | 7 | 8 |

**Salida esperada:**
- Resultado:
  | 6 | 8 |
  |---|---|
  |10 |12 |
- Pasos:
  - (1+5)=6, (2+6)=8, (3+7)=10, (4+8)=12

---

## Multiplicación de Matrices

**Entrada:**
- Matriz A:
  | 1 | 2 |
  |---|---|
  | 3 | 4 |
- Matriz B:
  | 2 | 0 |
  |---|---|
  | 1 | 2 |

**Salida esperada:**
- Resultado:
  | 4 | 4 |
  |---|---|
  |10 | 8 |
- Pasos:
  - (1*2+2*1)=4, (1*0+2*2)=4, (3*2+4*1)=10, (3*0+4*2)=8

---

## Determinante de Matriz 3x3

**Entrada:**
- Matriz:
  | 1 | 2 | 3 |
  |---|---|---|
  | 0 | 1 | 4 |
  | 5 | 6 | 0 |

**Salida esperada:**
- Determinante: 1*(1*0-4*6) - 2*(0*0-4*5) + 3*(0*6-1*5) = 1*(0-24) - 2*(0-20) + 3*(0-5) = -24 + 40 - 15 = 1
- Pasos: Expansión por cofactores.

---

## Inversa de Matriz 2x2

**Entrada:**
- Matriz:
  | 4 | 7 |
  |---|---|
  | 2 | 6 |

**Salida esperada:**
- Inversa:
  | 0.6 | -0.7 |
  |-----|------|
  | -0.2| 0.4  |
- Pasos: Cálculo de determinante, matriz adjunta y división por determinante.

---

## Resolución de Sistema (Gauss)

**Entrada:**
- Matriz aumentada:
  | 2 | 1 | 5 |
  |---|---|---|
  | 4 | 4 | 16|

**Salida esperada:**
- Solución: x=2, y=1
- Pasos: Eliminación de variables, sustitución regresiva.

---

Estos ejemplos pueden ser ampliados con más casos y variantes según necesidad docente o de pruebas.

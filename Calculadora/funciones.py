def suma_matriz(matriz_A, matriz_B):

    validar_mismas_dimensiones(matriz_A, matriz_B)
    numero_filas   = len(matriz_A)
    numero_columnas = len(matriz_A[0])
    matriz_resultado = [[0]*numero_columnas for _ in range(numero_filas)]

    for i in range(numero_filas):
        for j in range(numero_columnas):
            matriz_resultado[i][j] = matriz_A[i][j] + matriz_B[i][j]

    return matriz_resultado

def resta_matriz(matriz_A, matriz_B):

    validar_mismas_dimensiones(matriz_A, matriz_B)
    numero_filas   = len(matriz_A)
    numero_columnas = len(matriz_A[0])
    matriz_resultado = [[0]*numero_columnas for _ in range(numero_filas)]

    for i in range(numero_filas):
        for j in range(numero_columnas):
            matriz_resultado[i][j] = matriz_A[i][j] - matriz_B[i][j]

    return matriz_resultado

def producto_matrices(matriz_A, matriz_B):

    validar_producto(matriz_A, matriz_B)
    filas_A    = len(matriz_A)
    columnas_A = len(matriz_A[0])
    columnas_B = len(matriz_B[0])
    matriz_resultado = [[0]*columnas_B for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += matriz_A[i][k] * matriz_B[k][j]
            matriz_resultado[i][j] = suma

    matriz_resultado = limpiar_matriz(matriz_resultado)

    return matriz_resultado

def determinante_matriz(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)
    matriz_copia = [fila[:] for fila in matriz_A]
    signo = 1

    for columna in range(tamaño):
        fila_pivote = max(range(columna, tamaño), key=lambda f: abs(matriz_copia[f][columna]))
        if round(abs(matriz_copia[fila_pivote][columna]), 6) == 0:
            return 0

        if fila_pivote != columna:
            matriz_copia[columna], matriz_copia[fila_pivote] = (matriz_copia[fila_pivote], matriz_copia[columna])
            signo *= -1

        for fila in range(columna + 1, tamaño):
            factor = matriz_copia[fila][columna] / matriz_copia[columna][columna]
            for columna_actual in range(columna, tamaño):
                matriz_copia[fila][columna_actual] -= (factor * matriz_copia[columna][columna_actual])

    determinante = signo
    for i in range(tamaño):
        determinante *= matriz_copia[i][i]

    return round(determinante, 4)

def inversa_matriz(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    matriz_aumentada = [matriz_A[fila][:] + [1.0 if fila == columna else 0 for columna in range(tamaño)] for fila in range(tamaño)]

    for indice_pivote in range(tamaño):
        fila_pivote = max(range(indice_pivote, tamaño), key=lambda fila: abs(matriz_aumentada[fila][indice_pivote]))

        if round(abs(matriz_aumentada[fila_pivote][indice_pivote]), 6) == 0:
            raise ValueError("La matriz no tiene inversa.")
        
        matriz_aumentada[indice_pivote], matriz_aumentada[fila_pivote] = (matriz_aumentada[fila_pivote], matriz_aumentada[indice_pivote])

        pivote = matriz_aumentada[indice_pivote][indice_pivote]
        for columna in range(2 * tamaño):
            matriz_aumentada[indice_pivote][columna] /= pivote

        for fila in range(tamaño):
            if fila == indice_pivote:
                continue
            factor = matriz_aumentada[fila][indice_pivote]
            for columna in range(2 * tamaño):
                matriz_aumentada[fila][columna] -= (factor * matriz_aumentada[indice_pivote][columna])

    matriz_inversa = [matriz_aumentada[fila][tamaño:2*tamaño] for fila in range(tamaño)]
    matriz_inversa = limpiar_matriz(matriz_inversa)

    return matriz_inversa

def factorizacion_LU(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    matriz_L = [[0] * tamaño for _ in range(tamaño)]
    matriz_U = [fila[:] for fila in matriz_A]

    for indice in range(tamaño):
        matriz_L[indice][indice] = 1.0

    for columna in range(tamaño):
        pivote = matriz_U[columna][columna]

        if round(abs(pivote), 6) == 0:
            raise ValueError(f"Pivote cero en columna {columna}")
        
        for fila in range(columna + 1, tamaño):
            multiplicador = (matriz_U[fila][columna] / pivote)
            matriz_L[fila][columna] = multiplicador

            for indice_k in range(columna, tamaño):
                matriz_U[fila][indice_k] -= (multiplicador * matriz_U[columna][indice_k])

    matriz_L = limpiar_matriz(matriz_L)
    matriz_U = limpiar_matriz(matriz_U)

    return matriz_L, matriz_U

def resolver_sistema_gauss(matriz_coeficientes, vector_terminos):

    validar_cuadrada(matriz_coeficientes)
    numero_ecuaciones = len(matriz_coeficientes)
    if len(vector_terminos) != numero_ecuaciones:
        raise ValueError("El vector de términos independientes debe tener longitud n")

    matriz_aumentada = [matriz_coeficientes[fila][:] + [vector_terminos[fila]] for fila in range(numero_ecuaciones)]

    for columna in range(numero_ecuaciones):
        fila_pivote = max(range(columna, numero_ecuaciones), key=lambda f: abs(matriz_aumentada[f][columna]))

        if round(abs(matriz_aumentada[fila_pivote][columna]), 6) == 0:
            raise ValueError("El sistema es singular o mal condicionado")
        matriz_aumentada[columna], matriz_aumentada[fila_pivote] = (matriz_aumentada[fila_pivote], matriz_aumentada[columna]
                                                                           )
        for fila in range(columna + 1, numero_ecuaciones):
            coef_multiplicador = (matriz_aumentada[fila][columna]/ matriz_aumentada[columna][columna])
            for columna_aumentada in range(columna, numero_ecuaciones + 1):
                matriz_aumentada[fila][columna_aumentada] -= (coef_multiplicador * matriz_aumentada[columna][columna_aumentada])

    solucion = [0] * numero_ecuaciones
    for fila in range(numero_ecuaciones - 1, -1, -1):
        suma_conocidos = sum(matriz_aumentada[fila][col] * solucion[col] for col in range(fila + 1, numero_ecuaciones))
        solucion[fila] = (matriz_aumentada[fila][numero_ecuaciones] - suma_conocidos) / matriz_aumentada[fila][fila]

    return solucion

# validaciones

def validar_mismas_dimensiones(A, B):
    if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Las matrices deben tener las mismas dimensiones m×n.")

def validar_cuadrada(A):
    n = len(A)
    if any(len(fil) != n for fil in A):
        raise ValueError("La matriz debe ser cuadrada (n×n).")

def validar_producto(A, B):
    filas_A, cols_A = len(A), len(A[0])
    filas_B, cols_B = len(B), len(B[0])

    for i, fila in enumerate(A):
        if len(fila) != cols_A:
            raise ValueError(f"Matriz A no es rectangular en la fila {i}.")
        
    for j, fila in enumerate(B):
        if len(fila) != cols_B:
            raise ValueError(f"Matriz B no es rectangular en la fila {j}.")
        
    if cols_A != filas_B:
        raise ValueError(f"No se puede multiplicar A({filas_A}×{cols_A}) por " f"B({filas_B}×{cols_B}).")

def limpiar_matriz(matriz, decimales=4):
    return [[round(v, decimales) for v in fila] for fila in matriz]
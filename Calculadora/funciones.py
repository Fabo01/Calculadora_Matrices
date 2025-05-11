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

    return matriz_resultado

def determinante_matriz(matriz_A):
 
    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    matriz_copia = [fila[:] for fila in matriz_A]
    signo = 1

    for columna in range(tamaño):
        fila_pivote = max(range(columna, tamaño), key=lambda fila: abs(matriz_copia[fila][columna]))

        if abs(matriz_copia[fila_pivote][columna]) < 1e-12: # 1e- 12 es aproximado a cero para evitar errores de redondeo
            return 0.0

        if fila_pivote != columna:
            matriz_copia[columna], matriz_copia[fila_pivote] = (matriz_copia[fila_pivote], matriz_copia[columna])
            signo *= -1

        for fila in range(columna + 1, tamaño):
            factor = (matriz_copia[fila][columna]/ matriz_copia[columna][columna])
            for columna in range(columna, tamaño):
                matriz_copia[fila][columna] -= (factor * matriz_copia[columna][columna])

    determinante = signo
    for i in range(tamaño):
        determinante *= matriz_copia[i][i]

    return determinante


def inversa_matriz(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    matriz_aumentada = [matriz_A[fila][:] + [1.0 if fila == columna else 0.0 for columna in range(tamaño)] for fila in range(tamaño)]

    for indice_pivote in range(tamaño):
        fila_pivote = max(range(indice_pivote, tamaño), key=lambda fila: abs(matriz_aumentada[fila][indice_pivote]))

        if abs(matriz_aumentada[fila_pivote][indice_pivote]) < 1e-12:
            raise ValueError("Matriz singular, no tiene inversa.")
        
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

    return matriz_inversa

def factorizacion_LU(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    matriz_L = [[0.0] * tamaño for _ in range(tamaño)]
    matriz_U = [fila[:] for fila in matriz_A]

    for indice in range(tamaño):
        matriz_L[indice][indice] = 1.0

    for columna in range(tamaño):
        pivote = matriz_U[columna][columna]

        if abs(pivote) < 1e-12:
            raise ValueError(f"Pivote cero o muy pequeño en columna {columna}")
        
        for fila in range(columna + 1, tamaño):
            multiplicador = (matriz_U[fila][columna] / pivote)
            matriz_L[fila][columna] = multiplicador

            for indice_k in range(columna, tamaño):
                matriz_U[fila][indice_k] -= (multiplicador * matriz_U[columna][indice_k])

    return matriz_L, matriz_U


def resolver_sistema_gauss(matriz_coeficientes, vector_terminos):

    validar_cuadrada(matriz_coeficientes)
    numero_ecuaciones = len(matriz_coeficientes)
    if len(vector_terminos) != numero_ecuaciones:
        raise ValueError("El vector de términos independientes debe tener longitud n")

    matriz_aumentada = [matriz_coeficientes[fila][:] + [vector_terminos[fila]] for fila in range(numero_ecuaciones)]

    for columna in range(numero_ecuaciones):
        fila_pivote = max(range(columna, numero_ecuaciones), key=lambda f: abs(matriz_aumentada[f][columna]))

        if abs(matriz_aumentada[fila_pivote][columna]) < 1e-12:
            raise ValueError("El sistema es singular o mal condicionado")
        matriz_aumentada[columna], matriz_aumentada[fila_pivote] = (matriz_aumentada[fila_pivote], matriz_aumentada[columna]
                                                                           )
        for fila in range(columna + 1, numero_ecuaciones):
            coef_multiplicador = (matriz_aumentada[fila][columna]/ matriz_aumentada[columna][columna])
            for columna_aumentada in range(columna, numero_ecuaciones + 1):
                matriz_aumentada[fila][columna_aumentada] -= (coef_multiplicador * matriz_aumentada[columna][columna_aumentada])

    solucion = [0.0] * numero_ecuaciones
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
    if cols_A != filas_B:
        raise ValueError("Columnas de A deben coincidir con filas de B para multiplicar.")
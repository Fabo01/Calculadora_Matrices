def suma_matriz(matriz_A, matriz_B):

    # 1) Validar dimensiones
    num_filas = len(matriz_A)
    num_columnas = len(matriz_A[0])
    if len(matriz_B) != num_filas or any(len(fila) != num_columnas for fila in matriz_B):
        raise ValueError("Las matrices deben tener las mismas dimensiones m x n")

    # 2) Inicializar matriz resultado con ceros
    matriz_resultado = []
    for fila in range(num_filas):
        matriz_resultado.append([0] * num_columnas)

    # 3) Sumar elemento a elemento
    for fila in range(num_filas):
        for columna in range(num_columnas):
            valor_A = matriz_A[fila][columna]
            valor_B = matriz_B[fila][columna]
            valor_suma = valor_A + valor_B
            matriz_resultado[fila][columna] = valor_suma

    return matriz_resultado

def resta_matriz(matriz_A, matriz_B):

    # 1) Validar dimensiones
    num_filas = len(matriz_A)
    num_columnas = len(matriz_A[0])
    if len(matriz_B) != num_filas or any(len(fila) != num_columnas for fila in matriz_B):
        raise ValueError("Las matrices deben tener las mismas dimensiones m x n")

    # 2) Inicializar matriz resultado con ceros
    matriz_resultado = []
    for fila in range(num_filas):
        matriz_resultado.append([0] * num_columnas)

    # 3) Restar elemento a elemento
    for fila in range(num_filas):
        for columna in range(num_columnas):
            valor_A = matriz_A[fila][columna]
            valor_B = matriz_B[fila][columna]
            valor_resta = valor_A - valor_B
            matriz_resultado[fila][columna] = valor_resta

    return matriz_resultado

def producto_matrices(matriz_A, matriz_B):

    # 1) Obtener dimensiones
    filas_A = len(matriz_A)
    columnas_A = len(matriz_A[0])
    if any(len(fila) != columnas_A for fila in matriz_A):
        raise ValueError("La matriz A no es rectangular")
    if len(matriz_B) == 0 or any(len(fila) != len(matriz_B[0]) for fila in matriz_B):
        raise ValueError("La matriz B no es rectangular")
    filas_B = len(matriz_B)
    columnas_B = len(matriz_B[0])
    if filas_B != columnas_A:
        raise ValueError("El número de columnas de A debe coincidir con el número de filas de B")

    # 2) Inicializar matriz resultado con ceros
    matriz_resultado = []
    for fila in range(filas_A):
        matriz_resultado.append([0] * columnas_B)

    # 3) Producto punto elemento a elemento
    for fila in range(filas_A):
        for columna in range(columnas_B):
            suma_acumulada = 0
            for indice_multiplicador in range(columnas_A):
                valor_A = matriz_A[fila][indice_multiplicador]
                valor_B = matriz_B[indice_multiplicador][columna]
                producto = valor_A * valor_B
                suma_acumulada += producto
            matriz_resultado[fila][columna] = suma_acumulada

    return matriz_resultado

def inversa_matriz(matriz_A):

    # 1) Validar que A sea cuadrada
    n = len(matriz_A)
    if any(len(fila) != n for fila in matriz_A):
        raise ValueError("La matriz debe ser cuadrada (n×n).")
    
    # 2) Crear matriz aumentada [A | I]
    # Copiar fila a fila para no modificar matriz_A original
    matriz_aumentada = []
    for i in range(n):
        fila_A = list(matriz_A[i])               # copia de A
        fila_I = [1.0 if i == j else 0.0 for j in range(n)]
        matriz_aumentada.append(fila_A + fila_I)
    
    # 3) Eliminación Gauss–Jordan
    for pivote_indice in range(n):
        # 3.1) Encontrar pivote y, si es cero, intercambiar con fila inferior
        pivote = matriz_aumentada[pivote_indice][pivote_indice]
        if abs(pivote) < 1e-12:
            # buscar fila k>i con elemento no cero en la misma columna
            fila_intercambio = None
            for k in range(pivote_indice+1, n):
                if abs(matriz_aumentada[k][pivote_indice]) > 1e-12:
                    fila_intercambio = k
                    break
            if fila_intercambio is None:
                raise ValueError("La matriz es singular y no tiene inversa.")
            # intercambiar filas
            matriz_aumentada[pivote_indice], matriz_aumentada[fila_intercambio] = \
                matriz_aumentada[fila_intercambio], matriz_aumentada[pivote_indice]
            pivote = matriz_aumentada[pivote_indice][pivote_indice]
        
        # 3.2) Normalizar la fila del pivote (hacer 1 en diagonal)
        for col in range(2*n):
            matriz_aumentada[pivote_indice][col] /= pivote
        
        # 3.3) Eliminar todos los demás elementos de la columna del pivote
        for fila in range(n):
            if fila == pivote_indice:
                continue
            factor = matriz_aumentada[fila][pivote_indice]
            # restar factor * fila_pivote a la fila actual
            for col in range(2*n):
                matriz_aumentada[fila][col] -= factor * matriz_aumentada[pivote_indice][col]
    
    # 4) Extraer la parte derecha de la matriz aumentada → inversa
    matriz_inversa = []
    for i in range(n):
        # columnas n a 2n-1
        fila_inv = matriz_aumentada[i][n:2*n]
        matriz_inversa.append(fila_inv)
    
    return matriz_inversa

def determinante_matriz(matriz_A):

    # 1) Validar que A sea cuadrada
    n = len(matriz_A)
    if n == 0 or any(len(fila) != n for fila in matriz_A):
        raise ValueError("La matriz debe ser cuadrada (n×n).")

    # 2) Copiar A para no modificar la original
    A = [list(fila) for fila in matriz_A]
    signo = 1      # registro de intercambios de filas

    # 3) Eliminación hacia adelante con pivotaje parcial
    for i in range(n):
        # 3.1) Buscar fila de pivote (valor máximo absoluto en columna i)
        fila_pivote = max(range(i, n), key=lambda k: abs(A[k][i]))
        if abs(A[fila_pivote][i]) < 1e-12:
            return 0.0  # columna de ceros => determinante cero

        # 3.2) Si la fila de pivote no es i, intercambiar y cambiar signo
        if fila_pivote != i:
            A[i], A[fila_pivote] = A[fila_pivote], A[i]
            signo *= -1

        # 3.3) Anular abajo del pivote
        for fila in range(i+1, n):
            factor = A[fila][i] / A[i][i]
            # restar factor * fila_pivote a la fila actual
            for col in range(i, n):
                A[fila][col] -= factor * A[i][col]

    # 4) Determinante = signo * producto de diagonales
    det = signo
    for i in range(n):
        det *= A[i][i]
    return det

def factorizacion_LU(A):

    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    U = [row[:] for row in A]
    for i in range(n):
        L[i][i] = 1.0

    # Recorrer columnas
    for j in range(n):
        # Para cada fila i > j, calcular el multiplicador y eliminar
        pivot = U[j][j]
        if pivot is None or pivot == 0:
            raise ValueError(f"Pivote nulo en columna {j}, requiere pivotaje.")
        for i in range(j+1, n):
            m = U[i][j] / pivot    # multiplicador
            L[i][j] = m
            # Restar m * fila j de la fila i en U
            for k in range(j, n):
                U[i][k] -= m * U[j][k]

    return L, U
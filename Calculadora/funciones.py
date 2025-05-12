def suma_matriz(matriz_A, matriz_B):

    validar_mismas_dimensiones(matriz_A, matriz_B)
    numero_filas   = len(matriz_A) #obtiene numero filas
    numero_columnas = len(matriz_A[0]) #obtiene numero columnas
    matriz_resultado = [[0]*numero_columnas for _ in range(numero_filas)]#crea matriz vacia(rellena con ceros)para almacenar resultado

    for i in range(numero_filas):
        for j in range(numero_columnas):
            #suma cada elemento de la matriz A con el elemento en la misma posicion de la matriz B 
            #y lo almacena en la matriz resultado
            matriz_resultado[i][j] = matriz_A[i][j] + matriz_B[i][j]

    return matriz_resultado

def resta_matriz(matriz_A, matriz_B):

    validar_mismas_dimensiones(matriz_A, matriz_B)
    numero_filas   = len(matriz_A)
    numero_columnas = len(matriz_A[0])
    matriz_resultado = [[0]*numero_columnas for _ in range(numero_filas)]

    for i in range(numero_filas):
        for j in range(numero_columnas):
            #resta cada elemento de la matriz A con el elemento en la misma posicion de la matriz B
            matriz_resultado[i][j] = matriz_A[i][j] - matriz_B[i][j]

    return matriz_resultado

#funcion para multiplicar matrices
def producto_matrices(matriz_A, matriz_B):

    validar_producto(matriz_A, matriz_B)#validamos que las matrices sean compatibles para multiplicar
    filas_A    = len(matriz_A) 
    columnas_A = len(matriz_A[0])
    columnas_B = len(matriz_B[0])

    matriz_resultado = [[0]*columnas_B for _ in range(filas_A)] #crea matriz vacia para almacenar resultado

    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):#se recorre la fila de A y la columna de B
                suma += matriz_A[i][k] * matriz_B[k][j] #calcula el producto de la fila de A por la columna de B
            matriz_resultado[i][j] = suma

    return matriz_resultado

def determinante_matriz(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A) #obtiene el tamaño de la matriz
    matriz_copia = [fila[:] for fila in matriz_A] #se hace una copia de la matriz para no modificar la original
    signo = 1 #inicializa el signo del determinante

    for columna in range(tamaño):
        fila_pivote = max(range(columna, tamaño), key=lambda f: abs(matriz_copia[f][columna])) #busca el pivote maximo en la columna
        if round(abs(matriz_copia[fila_pivote][columna]), 6) == 0:#verifica si el pivote es cero
            return 0 #si el pivote es cero, el determinante es cero

        if fila_pivote != columna: #si el pivote no es la fila actual
            #intercambia la fila pivote con la fila actual
            matriz_copia[columna], matriz_copia[fila_pivote] = (matriz_copia[fila_pivote], matriz_copia[columna])
            signo *= -1 #cambia el signo del determinante
        #bloque que realiza eliminacion de gauss
        for fila in range(columna + 1, tamaño): #recorre las filas debajo del pivote
            factor = matriz_copia[fila][columna] / matriz_copia[columna][columna]#se calcula el factor de la fila
            for columna_actual in range(columna, tamaño): #recorre las columnas de la fila
                #se resta el factor de la fila actual por el pivote
                matriz_copia[fila][columna_actual] -= (factor * matriz_copia[columna][columna_actual])

    #calcula el determinante multiplicando los elementos de la diagonal principal
    determinante = signo
    for i in range(tamaño):
        determinante *= matriz_copia[i][i]
    #redondea el resultado a 4 decimales
    return round(determinante, 4)

def inversa_matriz(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    #se crea una matriz aumentada que contiene la matriz A y la matriz identidad
    matriz_aumentada = [matriz_A[fila][:] + [1.0 if fila == columna else 0 for columna in range(tamaño)] for fila in range(tamaño)]

    for indice_pivote in range(tamaño):
        #busca el pivote maximo en la columna
        fila_pivote = max(range(indice_pivote, tamaño), key=lambda fila: abs(matriz_aumentada[fila][indice_pivote]))

        if round(abs(matriz_aumentada[fila_pivote][indice_pivote]), 6) == 0:#si el pivote es cero, la matriz no tiene inversa
            raise ValueError("La matriz no tiene inversa.")
        #intercambia la fila pivote con la fila actual
        matriz_aumentada[indice_pivote], matriz_aumentada[fila_pivote] = (matriz_aumentada[fila_pivote], matriz_aumentada[indice_pivote])

        pivote = matriz_aumentada[indice_pivote][indice_pivote]#se obtiene el pivote
        for columna in range(2 * tamaño):#recorre las columnas del pivote
            matriz_aumentada[indice_pivote][columna] /= pivote#se divide el pivote por si mismo para que sea 1
        
        for fila in range(tamaño): #recorre las filas de la matriz
            if fila == indice_pivote: #si la fila es la fila pivote, se salta
                continue
            factor = matriz_aumentada[fila][indice_pivote] #se obtiene el factor de la fila
            for columna in range(2 * tamaño): 
                #se resta el factor de la fila actual por el pivote
                matriz_aumentada[fila][columna] -= (factor * matriz_aumentada[indice_pivote][columna])
    #se obtiene la matriz inversa de la matriz aumentada
    matriz_inversa = [matriz_aumentada[fila][tamaño:2*tamaño] for fila in range(tamaño)]
    matriz_inversa = limpiar_matriz(matriz_inversa) #llama a la funcion limpiar_matriz para redondear los resultados

    return matriz_inversa

def factorizacion_LU(matriz_A):

    validar_cuadrada(matriz_A)
    tamaño = len(matriz_A)

    matriz_L = [[0] * tamaño for _ in range(tamaño)]# crea matriz L con ceros
    matriz_U = [fila[:] for fila in matriz_A]# crea matriz U como copia de A

    # Inicializa la diagonal de L en 1
    for indice in range(tamaño):#
        matriz_L[indice][indice] = 1.0
    
    for columna in range(tamaño):
        pivote = matriz_U[columna][columna]#obtiene el pivote de la columna
        
        if round(abs(pivote), 6) == 0:#verifica que no haya un pivote cero
            raise ValueError(f"Pivote cero en columna {columna}")
        
        for fila in range(columna + 1, tamaño):#recorre las filas debajo del pivote
            multiplicador = (matriz_U[fila][columna] / pivote) #calcula el multiplicador de la fila actual
            matriz_L[fila][columna] = multiplicador #almacena el multiplicador en la matriz L

            for indice_k in range(columna, tamaño): #recorre las columnas del pivote
                #resta el multiplicador de la fila actual por el pivote
                matriz_U[fila][indice_k] -= (multiplicador * matriz_U[columna][indice_k]) 
    # Redondea los resultados a 4 decimales
    matriz_L = limpiar_matriz(matriz_L)
    matriz_U = limpiar_matriz(matriz_U)

    return matriz_L, matriz_U

#funcion para resolver un sistema de ecuaciones lineales Ax = b
def resolver_sistema_gauss(matriz_coeficientes, vector_terminos):

    validar_cuadrada(matriz_coeficientes)
    numero_ecuaciones = len(matriz_coeficientes) #obtiene los elementos de la matriz
    #verifica que el vector de terminos independientes tenga la misma longitud que la matriz
    if len(vector_terminos) != numero_ecuaciones: 
        raise ValueError("El vector de términos independientes debe tener longitud n")
    #se crea una matriz aumentada que contiene la matriz A y el vector b
    matriz_aumentada = [matriz_coeficientes[fila][:] + [vector_terminos[fila]] for fila in range(numero_ecuaciones)]

    for columna in range(numero_ecuaciones):
        #busca el pivote maximo en la columna
        fila_pivote = max(range(columna, numero_ecuaciones), key=lambda f: abs(matriz_aumentada[f][columna]))
        #verifica que el pivote no sea cero
        if round(abs(matriz_aumentada[fila_pivote][columna]), 6) == 0:
            raise ValueError("El sistema es singular o mal condicionado")
        #intercambia la fila pivote con la fila actual
        matriz_aumentada[columna], matriz_aumentada[fila_pivote] = (matriz_aumentada[fila_pivote], matriz_aumentada[columna]
                                                                           )
        for fila in range(columna + 1, numero_ecuaciones): #recorre las filas debajo del pivote
            #calcula el coeficiente multiplicador de la fila actual
            coef_multiplicador = (matriz_aumentada[fila][columna]/ matriz_aumentada[columna][columna]) 
            for columna_aumentada in range(columna, numero_ecuaciones + 1):#recorre las columnas del pivote
                #resta el coeficiente multiplicador de la fila actual por el pivote
                matriz_aumentada[fila][columna_aumentada] -= (coef_multiplicador * matriz_aumentada[columna][columna_aumentada])
    #se crea un vector solucion para almacenar los resultados
    solucion = [0] * numero_ecuaciones
    for fila in range(numero_ecuaciones - 1, -1, -1): #recorre las filas de la matriz aumentada
        #suma los elementos conocidos de la fila actual
        suma_conocidos = sum(matriz_aumentada[fila][col] * solucion[col] for col in range(fila + 1, numero_ecuaciones))
        #calcula la solucion de la fila actual
        solucion[fila] = (matriz_aumentada[fila][numero_ecuaciones] - suma_conocidos) / matriz_aumentada[fila][fila]

    return solucion

# validaciones

def validar_mismas_dimensiones(A, B):
    # Verifica que las matrices tengan las mismas dimensiones
    if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Las matrices deben tener las mismas dimensiones m×n.")

def validar_cuadrada(A):
    n = len(A) # Obtiene el número de filas de la matriz 
    if any(len(fil) != n for fil in A): # Verifica que la matriz sea cuadrada
        raise ValueError("La matriz debe ser cuadrada (n×n).")

def validar_producto(A, B):
    # Verifica que las matrices sean compatibles para multiplicar
    filas_A, cols_A = len(A), len(A[0])
    filas_B, cols_B = len(B), len(B[0])
    
    for i, fila in enumerate(A):
        if len(fila) != cols_A: # Verifica que la matriz A sea rectangular
            raise ValueError(f"Matriz A no es rectangular en la fila {i}.")
        
    for j, fila in enumerate(B):
        if len(fila) != cols_B: #verifica que la matriz B sea rectangular
            raise ValueError(f"Matriz B no es rectangular en la fila {j}.")
        
    if cols_A != filas_B: # Verifica que el número de columnas de A sea igual al número de filas de 
        raise ValueError(f"No se puede multiplicar A({filas_A}×{cols_A}) por " f"B({filas_B}×{cols_B}).")

def limpiar_matriz(matriz, decimales=4): 
    return [[round(v, decimales) for v in fila] for fila in matriz]#redondea los resultados a 4 decimales
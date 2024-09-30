# 1. Búsqueda Lineal - Números Pares:
def busqueda_lineal_pares(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            return lista[i]
    return -1

print(f'Primer número par: {busqueda_lineal_pares([1,3,5,7,9,2,4,6,8,10])}')

# 2. Búsqueda Binaria - Raíz Cuadrada:
def busqueda_binaria_raiz_cuadrada(numero):
    if numero < 0:
        return -1  # No se puede encontrar la raíz cuadrada de un número negativo

    inicio, fin = 0, numero
    while inicio <= fin:
        medio = (inicio + fin) // 2
        cuadrado = medio * medio

        if cuadrado == numero:
            return medio
        elif cuadrado < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
    return fin

print(f'Raíz cuadrada de 16: {busqueda_binaria_raiz_cuadrada(16)}')

# 3. Búsqueda Lineal - Elemento Mayoritario:
def busqueda_lineal_mayoritario(lista):
    contador = {}
    for num in lista:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1

        if contador[num] > len(lista) // 2:
            return num
    return -1

print(f'Elemento mayoritario: {busqueda_lineal_mayoritario([3,3,4,2,4,4,2,4,4])}')

# 4. Búsqueda Binaria - Punto de Inflexión:
def busqueda_binaria_punto_inflexion(lista):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] < lista[medio + 1]:
            izquierda = medio + 1

        else:
            derecha = medio    
    return lista[izquierda]

print(f'Punto de inflexión: {busqueda_binaria_punto_inflexion([1, 3, 8, 12, 4, 2])}')

# 5. Búsqueda Lineal - Subcadena:
def busqueda_lineal_subcadena(cadena, subcadena):
    ocurrencias = []
    subcadena_len = len(subcadena)
    
    for i in range(len(cadena) - subcadena_len + 1):
        if cadena[i:i + subcadena_len] == subcadena:
            ocurrencias.append(i)
    return ocurrencias

print(f'Ocurrencias de "ana" en "banana": {busqueda_lineal_subcadena("banana", "ana")}')

# 6. Búsqueda Binaria - Elemento Rotado:
def busqueda_binaria_elemento_rotado(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio
        
        if lista[izquierda] <= lista[medio]:
            if lista[izquierda] <= objetivo < lista[medio]:
                derecha = medio - 1
            else:
                izquierda = medio + 1
        else:
            if lista[medio] < objetivo <= lista[derecha]:
                izquierda = medio + 1
            else:
                derecha = medio - 1
    
    return -1

print(f'Índice del elemento 0 en [4,5,6,7,0,1,2]: {busqueda_binaria_elemento_rotado([4,5,6,7,0,1,2], 0)}')

# 7. Búsqueda Lineal - Elemento Único:
def busqueda_lineal_elemento_unico(lista):
    resultado = 0
    for num in lista:
        resultado ^= num
    return resultado

print(f'Elemento único: {busqueda_lineal_elemento_unico([2, 3, 5, 4, 5, 3, 4])}')

# 8. Búsqueda Binaria - Primer Ocurrencia:
def busqueda_binaria_primera_ocurrencia(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            resultado = medio
            derecha = medio - 1  # Sigue buscando en la mitad izquierda
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return resultado

print(f'Índice de la primera ocurrencia: {busqueda_binaria_primera_ocurrencia([1, 2, 4, 4, 4, 5, 6], 4)}')

# 10. Búsqueda Binaria - Pico en Montaña:
def busqueda_binaria_pico_montana(lista):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] < lista[medio + 1]:
            izquierda = medio + 1
        else:
            derecha = medio
    
    return lista[izquierda]

print(f'Pico en montaña: {busqueda_binaria_pico_montana([1, 3, 8, 12, 4, 2])}')
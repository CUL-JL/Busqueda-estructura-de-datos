def busqueda_binaria(lista, objeto):
    izquierda, derecha = 0, len(lista)-1
    while  izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objeto: return medio
        elif lista[medio] < objeto: izquierda = medio + 1
        else: izquierda = medio - 1
    return -1
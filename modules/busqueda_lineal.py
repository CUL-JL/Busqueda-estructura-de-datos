def busqueda_lineal(lista, objeto):
    for i in range(len(lista)):
        if lista[i] == objeto: return i # 1. if lista[i]%2 == 0
    return -1
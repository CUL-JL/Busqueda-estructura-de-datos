class BusquedaLineal:
    def __init__(self) -> None:
        pass
        
    # 1. Búsqueda Lineal - Números Pares:
    def pares(lista):
        for i in range(len(lista)):
            if lista[i] % 2 == 0:
                return lista[i]
        return -1

    # 3. Búsqueda Lineal - Elemento Mayoritario:
    def mayoritario(lista):
        contador = {}
        for numero in lista:
            if numero in contador:
                contador[numero] += 1
            else:
                contador[numero] = 1

            if contador[numero] > len(lista) // 2:
                return numero
        return -1

    # 5. Búsqueda Lineal - Subcadena:
    def subcadena(cadena, subcadena):
        ocurrencias = []
        subcadena_len = len(subcadena)
        
        for i in range(len(cadena) - subcadena_len + 1):
            if cadena[i:i + subcadena_len] == subcadena:
                ocurrencias.append(i)
        return ocurrencias

    # 7. Búsqueda Lineal - Elemento Único:
    def elemento_unico(lista):
        resultado = 0
        for numero in lista:
            resultado ^= numero
        return resultado

    # 9. Búsqueda Lineal - Suma de Dos:
    def suma_dos(lista, objetivo):
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] + lista[j] == objetivo:
                    return lista[i], lista[j]
        return -1
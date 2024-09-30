class BusquedaBinaria:
    def __init__(self) -> None:
        pass

    # 2. Búsqueda Binaria - Raíz Cuadrada:
    def raiz_cuadrada(numero):
        if numero < 0:
            return -1  

        izquierda, derecha = 0, numero
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            cuadrado = medio * medio

            if cuadrado == numero:
                return medio
            elif cuadrado < numero:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return derecha

    # 4. Búsqueda Binaria - Punto de Inflexión:
    def punto_inflexion(lista):
        izquierda, derecha = 0, len(lista) - 1
        
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            
            if lista[medio] < lista[medio + 1]:
                izquierda = medio + 1

            else:
                derecha = medio    
        return lista[izquierda]

    # 6. Búsqueda Binaria - Elemento Rotado:
    def elemento_rotado(lista, objetivo):
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

    # 8. Búsqueda Binaria - Primer Ocurrencia:
    def primera_ocurrencia(lista, objetivo):
        izquierda, derecha = 0, len(lista) - 1
        resultado = -1
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            
            if lista[medio] == objetivo:
                resultado = medio
                derecha = medio - 1  
            elif lista[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        
        return resultado

    # 10. Búsqueda Binaria - Pico en Montaña:
    def pico_montana(lista):
        izquierda, derecha = 0, len(lista) - 1
        
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            
            if lista[medio] < lista[medio + 1]:
                izquierda = medio + 1
            else:
                derecha = medio
        
        return lista[izquierda]
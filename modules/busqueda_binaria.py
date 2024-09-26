
class BusquedaBinaria:
    def __init__(self, lista, fin):
        self.lista = None or lista
        self.inicio = 0
        self.fin = fin

    def raiz_cuadrada(self):
        izq, der = self.inicio, self.fin
        while izq <= der:
            mid = (izq + der) // 2
            if mid * mid <= self.fin:
                izq = mid + 1
            else:
                der = mid - 1
        return der
    
    def punto_de_inflexion(self):
        izq, der = 0, len(self.lista) - 1
        
        while izq < der:
            mid = (izq + der) // 2
            if self.lista[mid] > self.lista[mid + 1]: der = mid
            else: izq = mid + 1
        return izq
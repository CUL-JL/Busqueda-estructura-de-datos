class BusquedaLineal:
    def __init__(self, lista):
        self.lista = None or lista

    def primer_par(self, n):
        for i in range(len(self.lista)):
            if self.lista[i]%2 == 0: return self.lista[i]
        return -1
    
    def encontrar_mayoritario(self):
        candidato, contador = None, 0
        for n in self.lista:
            if contador == 0: candidato = n
            if n == candidato: contador += 1
            else: contador -= 1
        if self.lista.count(candidato) <= 2: pass
        return candidato

    def buscar_ocurrencias(cadena, subcadena):
        ocurrencias = []
        longitud_subcadena = len(subcadena)
        
        for i in range(len(cadena) - longitud_subcadena + 1):
            if cadena[i:i + longitud_subcadena] == subcadena:
                ocurrencias.append(i)
        
        return ocurrencias
from modules.binaria import BusquedaBinaria
from modules.lineal import BusquedaLineal
import random

# Funciones secundarias
def pedir_numero(num):
    while True: # Bucle
        try: return int(input(num)) # Retorno de valor numérico
        except ValueError: print('Error: ingreso de valor no numérico.\n') # Manejo de errores

def pedir_cadena(txt):
    while True: # Bucle
        try: return input(txt) # Retorno de valor numérico
        except ValueError: print('Error: ingreso de valor no valido.\n') # Manejo de errores

# Funciones principal
def ejecutar_opcion(opcion):
    match opcion:
        case 1:
            lista = [random.randint(1, 20) for _ in range(10)]
            print(f'Lista: {lista}\nPrimer elemento par de la lista : {BusquedaLineal.pares(lista)}\n')

        case 2:
            numero = pedir_numero('Ingrese un número: ')
            print(f'La raíz cuadrada de {numero} es {BusquedaBinaria.raiz_cuadrada(numero)}.\n')

        case 3:
            lista = [random.randint(1, 10) for _ in range(15)]
            print(f'Lista: {lista}\nElemento mayoritario de la lista: {BusquedaLineal.mayoritario(lista)}\n')
        
        case 4:
            lista = [random.randint(1, 10) for _ in range(5)]
            print(f'Lista: {lista}\nPunto de inflexión de la lista: {BusquedaBinaria.punto_inflexion(lista)}\n')

        case 5:
            cadena = pedir_cadena('Ingrese una cadena: ')
            subcadena = pedir_cadena('Ingrese una subcadena: ')
            print(f'Cadena: {cadena}\nSubcadena: {subcadena}\nOcurrencias: {BusquedaLineal.subcadena(cadena, subcadena)}\n')
        
        case 6:
            lista = [random.randint(1, 10) for _ in range(10)]
            objetivo = random.randint(1, 10)
            print(f'Lista: {lista}\nObjetivo: {objetivo}\nElemento rotado: {BusquedaBinaria.elemento_rotado(lista, objetivo)}\n')

        case 7:
            lista = [random.randint(1, 10) for _ in range(10)]
            print(f'Lista: {lista}\nElemento único de la lista: {BusquedaLineal.elemento_unico(lista)}\n')

        case 8:
            lista = [random.randint(1, 10) for _ in range(10)]
            objetivo = random.randint(1, 10)
            print(f'Lista: {lista}\nObjetivo: {objetivo}\nPrimer ocurrencia: {BusquedaBinaria.primera_ocurrencia(lista, objetivo)}\n')
        
        case 9:
            lista = [random.randint(1, 10) for _ in range(10)]
            objetivo = random.randint(1, 10)
            print(f'Lista: {lista}\nObjetivo: {objetivo}\nSuma de dos: {BusquedaLineal.suma_dos(lista, objetivo)}\n')

        case 10:
            lista = [random.randint(1, 10) for _ in range(10)]
            print(f'Lista: {lista}\nElemento pico de la lista: {BusquedaBinaria.pico(lista)}\n')
        
        case 11:
            print('Saliendo del programa...')
            exit()

        case _:
            print('Opción no válida.\n')
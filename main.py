from modules.menu import ejecutar_opcion

while True:
    try:
        ejecutar_opcion(int(input('Opciones de busqueda lineal o binaria:\n 1. Primer elemento par\n 2. Raíz cuadrada\n 3. Elemento mayoritario\n 4. Punto de inflexión\n 5. Subcadena\n 6. Elemento rotado\n 7. Elemento único\n 8. Primer ocurrencia\n 9. Suma de dos\n 10. Elemento pico\n 11. Salir del programa\nIngrese una opción: ')))
    except ValueError:
        print('\nError: Ingreso de valor no numerico.')
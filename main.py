from modules.busqueda_lineal import busqueda_lineal
from modules.busqueda_binaria import busqueda_binaria

# 1. 

list_elemnts = [3,1,4,6,7,5,9,10]
print(busqueda_lineal(list_elemnts, None))

# 2.
list_elemnts = [10,1,4,6,3,5,9,4]
print(busqueda_binaria(list_elemnts, 9))
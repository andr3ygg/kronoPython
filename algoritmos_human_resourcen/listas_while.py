import random

lista = []
posicion = 0

for i in range(10):
    lista.append(random.randint(1, 9))

longitud_lista = len(lista)
print(f"INPUT: {lista}")
while posicion < (longitud_lista - 1):
    """
    item1 = lista[posicion] # posicion = 0
    item2 = lista[posicion+1] # 0+1
    lista[posicion] = item2
    lista[posicion+1] = item1
    print(lista)
    """
    item1 = lista[posicion]  # posicion = 0
    item2 = lista[posicion + 1]  # 0+1
    print(f"{item2}  {item1}")
    posicion += 2
    # == for i in range(0,l,2)

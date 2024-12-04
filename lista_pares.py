# 7. Escribe una función para filtrar números pares en una lista

import random

def filtrar_pairs(lista):

    lista_pares = []

    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares


sample_list = []

for i in range(10):
    sample_list.append(random.randint(1, 100))

print(sample_list)
print(filtrar_pairs(sample_list))
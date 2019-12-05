import numpy as np

ilosc = int(input("Podaj ilosc elementow: "))
lista = []


def avg(l):
    suma = sum(l)
    avg = suma/len(l)
    return avg


def std(l):
    std = 0
    srednia = avg(l)
    for el in l:
        std += (el-srednia)**2
    std = (std/len(l))**0.5
    return std


for i in range(ilosc):
    lista.append(int(input("podaj element: ")))
print(avg(lista))
print(std(lista))
print(np.average(lista))
print(np.std(lista))




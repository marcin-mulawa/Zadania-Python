def suma(f, n):
    suma = 0
    for i in range(f, n+1):
        suma += i
    return suma


a = int(input("Podaj początek przedziału: "))
b = int(input("Podaj koniec przedziału: "))
print(suma(a, b))
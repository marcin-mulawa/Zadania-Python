from math import factorial


def newton(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def pascal(j):
    lista = []

    for i in range(j+1):
        lista.append(int(newton(j,i)))
    return lista


j = int(input("n"))
print(pascal(j))

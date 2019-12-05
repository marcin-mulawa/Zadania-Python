def silnia(n):
    silnia=1
    for i in range(1,n+1):
        silnia*=i
    return silnia

def silnia_rec(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*silnia_rec(n-1)
dec='t'
while dec =='t':
    n = int(input("podaj n: "))
    print(silnia(n))
    print(silnia_rec(n))
    dec=input('t/n: ')
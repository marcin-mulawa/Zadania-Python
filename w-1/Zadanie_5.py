import math

print('Znajdowanie miejsc zerowych trójmianu kwadratowego')
a=int(input('Podaj a: '))
b=int(input('Podaj b: '))
c=int(input('Podaj c: '))

delta = b**2 - 4*a*c

x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)
print('x1={}\nx2={}'.format(x1,x2))
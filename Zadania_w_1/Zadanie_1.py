def dzielniki(number):
    for i in range(1, number+1):
        if number%i==0:
            print(i)


number = int(input("Podaj liczbę której dzielniki mam wyświetlić: "))
dzielniki(number)
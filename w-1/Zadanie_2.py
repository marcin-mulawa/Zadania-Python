def wyswietl(number):
    for i in range(1,11):
        print('{} x {} = {}'.format(number,i,number*i))


number = float(input("Enter a number: "))
wyswietl(number)
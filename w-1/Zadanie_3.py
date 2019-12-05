def change_temp(temp):
    if temp[len(temp)-1] == 'C':
        print('{} = {}F'.format(temp, (int(temp[:-1])*9/5)+32))
    else:
        print('{} = {}C'.format(temp, (int(temp[:-1])-32)*5/9))


temp = input("Podaj temperaturę w formacie 12C lub 26F")
change_temp()
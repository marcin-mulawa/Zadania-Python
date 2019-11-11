def change_dist(dist, wybor):
    if wybor == 1:
        print('{}km = {}mil'.format(dist, dist * 0.621371192))
    elif wybor == 2:
        print('{}mil = {}km'.format(dist, dist * 1.609344))


decyzja = 't'

while decyzja == 't':
    try:
        wybor = int(input("wybierz:\n 1.Kilometry\n 2.Mile\nPodaj 1 lub 2"))
        if wybor != 1 and wybor != 2:
            print('You entered an invalid number')
            decyzja = input("czy wykonać jeszcze raz t/n")
        else:
            dec = 't'
            while dec == 't':
                try:
                    dist = float(input("Podaj dystans"))
                    change_dist(dist,wybor)
                    dec = 'n'
                except ValueError:
                    print('You entered an invalid number')
                    dec = input("czy wykonać jeszcze raz t/n")
    except ValueError:
        print('You entered an invalid number')
        decyzja = input("czy wykonać jeszcze raz t/n")
    decyzja = input("czy wykonać jeszcze raz t/n")
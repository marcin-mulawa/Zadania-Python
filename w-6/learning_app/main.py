import datetime
import glob


def read_file(file):
    with open(file) as f:
        f.read()


def create_file(file, data=None):
    if data is None:
        pass


def new_words(number):
    words = []
    for i in range(number):
        key = input("Pddaj klucz: ")
        value = input("Podaj wartość: ")
        words.append({'key': key, 'value': value, 'score': 0, 'time': datetime.date})
    return words


def menu():
    print("Witaj w programie do nauki słówek!!!\n"
          "Powiedz mi co chcszesz dzisiaj zrobić:\n"
          "1. Stworzyć nowy plik ze słowami do nauki.\n"
          "2. Uczyć się z istniejącego już pliku.")
    decision = int(input("Podaj 1 lub 2. "))
    if decision == 1:
        return decision
    elif decision == 2:
        print('Wybierz plik do nauki:')
        files = []

        for i, el in enumerate(glob.glob('./*.txt')):
            files.append((i, el.strip('.\\')))
        for i, el in files:
            print('{}. {}'.format(i+1, el))

        num_file = int(input("Wybór (wpisz liczbę): "))
        file = files[num_file-1][1]
        print("Podaj sposób nauki:\n"
              "1. Nauka przez wpisywanie."
              "2. Nauka przez pokazywanie")
        way = int(input("Sposób: "))
        return decision, file, way





def main_loop():
    m = menu()
    print(m)

main_loop()

from datetime import datetime
import glob
import random
import os.path
import keyboard

def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.split(';')
            line[3] = line[3].strip('\n')
            t = datetime.strptime(line[3], '%m/%d/%Y').date()
            words.append({'key': line[0], 'value': line[1], 'score': int(line[2]), 'time': t})
        return words


def edit_file(file):
    with open(file, 'a') as f:
        add_to_file(f)


def create_file(file):
    if not os.path.exists(file):
        decision = 't'
    else:
        decision = input("Plik istnieje, kontynuować? [t/n]")
    if decision == 't':
        with open(file, 'w') as f:
            add_to_file(f)


def new_words(number):
    words = []
    for i in range(number):
        key = input("Pddaj klucz: ")
        value = input("Podaj wartość: ")
        t = datetime.now()
        t = t.strftime("%m/%d/%Y")
        words.append({'key': key, 'value': value, 'score': 0, 'time': t})
    return words


def add_to_file(f, words=None):
    if words is None:
        while True:
            try:
                number = int(input('Podal liczbę słów, które chcesz utworzyć: '))
                break
            except:
                print('Nieprawidłowa liczba')
        words = new_words(number)
    for word in words:
        f.write("{};{};{};{}\n".format(word['key'], word['value'], word['score'], word['time']))


def choose_file():
    files = []
    for i, el in enumerate(glob.glob('./*.txt')):
        files.append((i, el.strip('.\\')))
    for i, el in files:
        print('{}. {}'.format(i + 1, el))
    num_file = int(input("Wybór (wpisz liczbę): "))
    file = files[num_file - 1][1]
    return file


def show_learn(words):
    pass


def write_learn(words, file):
    for word in words:
        if word['score'] < 5 or word['time'] - datetime.now().date() > 5:
            print(word['key'])
            good = word['value']
            ans = input("Wpisz wartośc: ")
            t = datetime.now()
            t = t.strftime("%m/%d/%Y")
            word['time'] = t
            if good == ans:
                print("Dobra odpowiedź")
                word['score']+=1
            else:
                print('Zła odpowiedź')
                word['score']-=1
    with open(file, 'w') as f:
        add_to_file(f, words)


def show_learn(words,file):
    for word in words:
        if word['score'] < 5 or word['time'] - datetime.now().date() > 5:
            print(word['key'])
            print('Naciśnij enter aby aby pokazać odpowiedz:')
            good = word['value']
            t = datetime.now()
            t = t.strftime("%m/%d/%Y")
            word['time'] = t
            if good == ans:
                word['score']+=1
            else:
                word['score']-=1
    with open(file, 'w') as f:
        add_to_file(f, words)



def learning(file):
    print("Podaj sposób nauki:\n"
          "1. Nauka przez wpisywanie."
          "2. Nauka przez pokazywanie")
    dec = int(input("Sposób: "))
    words = read_file(file)
    learn_list = []
    random.shuffle(words)
    if dec == 1:
        write_learn(words, file)



def menu():
    print("Witaj w programie do nauki słówek!!!\n"
          "Powiedz mi co chcszesz dzisiaj zrobić:\n"
          "1. Stworzyć nowy plik ze słowami do nauki.\n"
          "2. Dolączyć nowe słowa do pliku.\n"
          "3. Uczyć się z istniejącego już pliku.")
    while True:
        try:
            decision = int(input("Wybór (wpisz liczbę): "))
            return decision
        except:
            print("Podaj liczbę!")


def main_loop():
    decision = menu()
    if decision == 1:
        file = input("Podaj nazwę pliku, który chcesz stworzyć") + '.txt'
        create_file(file)
    elif decision == 2:
        print("Wybierz plik do edycji: ")
        file = choose_file()
        edit_file(file)
    elif decision == 3:
        print('Wybierz plik do nauki:')
        file = choose_file()
        learning(file)


main_loop()

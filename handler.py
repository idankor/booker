from colorama import Fore
from editor import *
from printer import *
from status import *
from editor import *


class Load():
    def __init__(self, data):
        if data == 'syn':
            data = 'synopsis'
        path = f'data/{data}.txt'
        f = open(path, 'r')
        string = f.read()
        f.close()
        temp_list = string.split("\n---\n")
        for item in temp_list:
            State.data.append(item)
        State.book = data
        print(
            Padder.clean(
                f'Loading {State.book} ...' + Fore.GREEN +
                ' OK' + Fore.RESET + '!'))
        print('')
        State.mode = 'Loaded'


class Pearler():
    def load():
        print(Padder.clean('Loading pearls...'), end='')
        State.pearls = []
        f = open('data/pearls.txt', 'r')
        string = f.read()
        f.close()
        temp_list = string.split('\n---\n')
        for item in temp_list:
            State.pearls.append(item)
        print(Fore.GREEN + ' OK' + Fore.RESET + '!')

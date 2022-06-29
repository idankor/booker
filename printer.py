from cleaner import *
from colorama import *
from editor import *
from padder import *


class Printer():

    def pearls():

        clear()

        for i in range(0, len(State.pearls) - 1):
            print(
                Padder.item(
                    Fore.CYAN + Padder.num(i) + Fore.RESET +
                    State.pearls[i]) + '\n')

    def clean(msg):
        print(Padder.clean(msg))

    def error(msg):
        print('')
        print(
            Padder.clean(
                msg=Fore.RED + 'Error' + Fore.RESET +
                ': ' + msg))
        print(' ' * 15 + 'Type \'h\' for help.\n')

    def workspace():
        clear()
        if len(State.workspace) == 1:
            print(Padder.marker(State.workspace[0]) + '\n')
        elif len(State.workspace) > 1:
            for i in range(0, len(State.workspace) - 1):
                print(
                    f' ' * 5 + f'[{i+1}] ' + Padder.item(State.workspace[i]))

from editor import *
from colorama import Fore, Style
from padder import *


class Status():
    def __init__(self):
        print(
            Padder.clean(
                Fore.LIGHTBLACK_EX + Style.DIM + 'Book:'),
            end='')
        print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
              f' {State.book}', end='    ' + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + Style.DIM + 'Mode:',
              end='')
        print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
              f' {State.mode}', end='')
        print(Style.RESET_ALL)

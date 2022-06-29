from handler import *
from cleaner import *
from random import randint
from editor import *
from status import *


class my_random_number():
    def __init__(self):
        self.idx = randint(0, len(State.data))


class Generator():
    fwd = 1
    bwd = 1
    position = 0
    idx = my_random_number()

    def new():
        State.screen = f'Random navigation mode ({State.book})'
        State.workspace = []
        if len(State.data) == 0:
            Printer.error('No data is loaded.')
        elif len(State.data) > 0:
            Generator.idx = randint(0, len(State.data) - 1)
            State.workspace.append(
                State.data[Generator.idx])
            Generator.position = 0
            Printer.workspace()
            State.mode = 'Random navigation'

    def next():
        print(State.workspace)
        # State.workspace.append(
        #  State.data[Generator.idx + Generator.fwd])
        Generator.fwd = Generator.fwd + 1

    def pearl():
        clear()
        State.screen = 'pearl'
        random_number = randint(0, len(State.pearls) - 1)
        print('\n' * 4)
        print(Padder.clean(
            State.pearls[random_number]) + '\n')
        Status()

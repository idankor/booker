from indenter import *
from colorama import Fore


class Error():
    def __init__(self, string):
        self.msg = Fore.RED + 'Error' + Fore.RESET + ': ' + string
        print(Indent.clean(self.msg))
        print(' ' * 13 + 'Type \'h\' for help.')

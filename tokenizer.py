from nltk.tokenize import sent_tokenize
from colorama import Fore
from indenter import *


class tknzr():
    def __init__(self, file):
        self.buffer = ''
        print(Indent.clean(f'Tokenizing {file}.txt...'))
        self.fh = open(f'data/{file}.txt', 'r')
        self.buffer = self.fh.read()
        self.fh.close()
        self.temp_list = sent_tokenize(
            self.buffer, language='english')
        self.fh = open(f'data/{file}.txt', 'w')
        self.fh.write('\n---\n'.join(self.temp_list))
        self.fh.close()
        print(Fore.GREEN + Indent.clean('Done') + Fore.RESET + '!')

from error import *
from generator import Generator
from printer import *
from handler import *
from cleaner import *
from tokenizer import *


class Cmd():
    def __init__(self, cmd, word_list):
        self.command = cmd
        self.words = word_list

        if self.command == 'error':
            Printer.error('No such command.')

        elif self.command == 'quit':
            if len(self.words) == 1:
                exit()
            elif len(self.words) > 1:
                Error('To quit, type only \'q\'.')

        elif self.command == 'pearls':
            Printer.pearls()

        elif self.command == 'pearl':
            Generator.pearl()

        elif self.command == 'clear':
            clear()

        elif self.command == 'tokenize':
            if len(self.words) > 1:
                tknzr(self.words[1])
            elif len(self.words) == 1:
                temp = input(
                    Indent.clean('Filename:') + ' ')
                tknzr(temp)

        elif self.command == 'load':
            if len(self.words) > 1:
                Load(self.words[1])
            elif len(self.words) == 1:
                if self.words[0] == 'syn':
                    Load('synopsis')
                elif self.words[0] == 'load' or self.words[0] == 'l':
                    Load(
                        input(
                            Indent.clean('Filename:') + ' '))
                else:
                    Load(self.words[0])

        elif self.command == 'new':
            Generator.new()

        elif self.command == 'next':
            Generator.next()

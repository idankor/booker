import textwrap
from colorama import *


class Padder():

    prefix = ''
    spaces = 15

    def num(counter):
        if counter + 1 < 10:
            Padder.prefix = f'[00{str(counter + 1)}]'
        elif counter + 1 > 9 and counter + 1 < 100:
            Padder.prefix = f'[0{str(counter + 1)}]'
        elif counter + 1 > 99 and counter + 1 < 1000:
            Padder.prefix = f'[{str(counter + 1)}]'
        Padder.prefix = Padder.prefix + '  '
        return Padder.prefix

    def clean(msg):
        pref_width = 60
        wrapper = textwrap.TextWrapper(
            initial_indent=' ' * Padder.spaces,
            width=pref_width, subsequent_indent=' ' *
            Padder.spaces)
        return wrapper.fill(msg)

    def item(msg):
        pref_width = 60
        wrapper = textwrap.TextWrapper(
            initial_indent='', width=pref_width,
            subsequent_indent=' ' * 13)
        return wrapper.fill(msg)

    def marker(msg):
        pref_width = 60
        wrapper = textwrap.TextWrapper(
            initial_indent='\t' + Fore.BLUE + '→ [1]' + Fore.RESET + ' ' * 2, width=pref_width,
            subsequent_indent=' ' * 15)
        return wrapper.fill(msg)

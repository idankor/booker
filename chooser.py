from padder import *
from colorama import Fore
from aliases import selector
from commander import *
from editor import *
from status import *


class Choose():
    def __init__(self):
        self.selected = 'init'
        self.words = []
        self.choice = ''
        Status()
        # Print '$'
        temp_string = Fore.BLUE + '$ ' + Fore.RESET
        # Take input from user
        self.choice = input(Padder.clean(temp_string))
        self.words = self.choice.split(' ')
        # Check if user's input is a known command
        # If it is, command's name is stored in 'selected'
        for item in selector.keys():
            for alias in selector[item]["aliases"]:
                if self.words[0] == alias:
                    self.selected = item
                    break
        # If no command is found, set 'selected' to 'error'
        if self.selected == 'init':
            self.selected = 'error'
        # If command exists, print this
        if self.selected != 'error':
            print('')
            print(
                Padder.clean(
                    Fore.CYAN + 'Running \'' + Fore.RESET +
                    self.selected + Fore.CYAN + '\'' + Fore.RESET))
        # Run command
        Cmd(self.selected, self.words)
        return Choose()

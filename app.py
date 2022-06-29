from handler import *
from padder import *
from cleaner import *
from chooser import *
from colorama import Fore, Style
from editor import *
import os

# Initialize some State vars
State.mode = 'Ready'
State.book = '-–'
State.data = []

# Clear screen
clear()

# Monitor progress and print output
print(
    Padder.clean(
        'Launching app... ' + Fore.GREEN + 'OK' +
        Fore.RESET + '!'))

# Load pearls
Pearler.load()

# Run Choose
print('')
Choose()

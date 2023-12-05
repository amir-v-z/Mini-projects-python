# pip install pyfiglet
# pip install termcolor
import pyfiglet
from termcolor import colored

text = colored(pyfiglet.figlet_format(input("Enter text: "), font='slant'), 'red')

print(text)
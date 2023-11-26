# pip install pyfiglet
# pip install termcolor
import pyfiglet
from termcolor import colored

text = colored(pyfiglet.figlet_format("Hello World", font='slant'), 'red')

print(text)
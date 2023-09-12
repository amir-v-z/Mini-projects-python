# The file name should not be translate
# Be sure to be connected to the Internet to run the program

# pip install translate
from translate import Translator
t1 = Translator(to_lang="persian")
t2 = Translator.translate(t1, input("Enter your text: "))
print(t2)
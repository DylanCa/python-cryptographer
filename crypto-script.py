import numpy
from pick import pick
from methods import Methods

# Asks the user to enter text
encrypted_text = input("Enter the encrypted text :\n$")

list_title = '{}'.format(
    "Please choose an ecryption method from this list :\n")
methods_list = ["Caesar Cipher", "ROT13", "Hill Cipher"]

methods_list, list_title = pick(methods_list, list_title)

if list_title == 0:
    Methods(encrypted_text).applyCaesarShift()

elif list_title == 1:
    Methods(encrypted_text).applyROT13()
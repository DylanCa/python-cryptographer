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
    list_title = '{}'.format("Do you want to decode or encode ?\n")
    methods_list = ["Decode", "Encode"]

    methods_list, list_title = pick(methods_list, list_title)

    if list_title == 0:
        Methods(encrypted_text).decodeCaesarCipher()

    elif list_title == 1:
        Methods(encrypted_text).encodeCaesarCipher()

elif list_title == 1:
    Methods(encrypted_text).encodeROT13()
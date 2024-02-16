import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def dechiffrer_cesar(message_chiffre):
    decalage = 1

    message_dechiffre = ""

    for char in message_chiffre:
        if char.isupper():
            lettre_dechiffree = chr((ord(char) - decalage - 65) % 26 + 65)
            message_dechiffre += lettre_dechiffree

        elif char.islower():
            lettre_dechiffree = chr((ord(char) - decalage - 97) % 26 + 97)
            message_dechiffre += lettre_dechiffree
        else:
            message_dechiffre += char

    return message_dechiffre

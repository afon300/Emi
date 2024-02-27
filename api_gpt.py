import os
import openai

file_path = 'C:\\Users\\antoi\\Documents\\github\\LaughWithGPT\\key_open_ai.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Contenu du fichier :\n{content}")
else:
    print(f"Le fichier {file_path} n'existe pas.")


def dechiffrer_cesar(message_chiffre):
    decalage = 3

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


################################################ API CHATGPT #################################################

def gpt(prompt):
    with open('key_open_ai.txt', 'r') as f:
        clé_chiffré = f.read()
        clé_déchiffré = dechiffrer_cesar(clé_chiffré)
    openai.api_key = clé_déchiffré
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )

    reponse = (completion['choices'][0]['message']['content'])
        
    return reponse
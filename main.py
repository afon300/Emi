from fonction_gpt import *
from fonctions import *

cls()
prompt = str(input("Entrez le prompt : "))
reponse = GPT(prompt)
print(reponse)
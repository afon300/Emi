import datetime
import time

from fonction_gpt import *
from fonctions import *

temps = datetime.datetime.now()
if temps.hour == 8 and temps.minute == 0 and temps.second == 0:
    cls()
    prompt = ("Tu est un utilisateur de Twitter, tu parle à tes amis, nous somme le", temps, "dis bonjour à tout le monde et souhaite leur de passer une bonne journée")
    reponse = GPT(prompt)
    print(reponse)
    time.sleep(1)

cls()
prompt1 = "Tu est un utilisateur de Twitter, fais des messages courts en moyenne 100 caractères. caractère, tu parle à tes amis, nous somme le"
prompt2 = "dis bonjour à tout le monde et souhaite leur de passer une bonne journée"
prompt = prompt1 + " " + str(temps) + " " + prompt2
reponse = GPT(prompt)
print(reponse)
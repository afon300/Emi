import datetime
import time
import random

from api_gpt import *
from fonctions import *

temps = datetime.datetime.now()
if temps.hour == 8 and temps.minute == 0 and temps.second == 0:
    cls()
    prompt = ("Tu est un utilisateur de Twitter, tu parle à tes amis, nous somme le", temps, "dis bonjour à tout le monde et souhaite leur de passer une bonne journée")
    reponse = GPT(prompt)
    print(reponse)
    time.sleep(1)

cls()
dico_prompt = {"dis bonjour à tout le monde et souhaite leur de passer une bonne journée" : 1, 
               "pause leur une question sur leur activité de la journée" : 2, 
               "demande comment vas être leur week-end" : 3, 
               "demande comment se passe leur week-end" : 4, 
               "demande leur comment se passe leur semaine" : 5,
               "demande leur se qu'il pense comment va être leur journée" : 6,
               "souhaite leur bonne chance pour leur journée" : 7
               }

prompt1 = "Tu est un utilisateur de Twitter, fais des messages courts en moyenne 100 caractères. caractère, tu parle à tes amis, nous somme le"
random_nb = random.randint(0, 7)
for prompt_du_dico, num in dico_prompt.items():
print(random_nb)
prompt = prompt1 + " " + str(temps) + " " + prompt2
reponse = GPT(prompt)
print(reponse)


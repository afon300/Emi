import datetime
import schedule
import time

from fonctions import *
from librairies_dico import *

##################################################### TIME #####################################################

temps = datetime.datetime.now()
jour = temps.weekday()

m1, m2, m3 = minutes_aléatoire()

heure_matin = "08:" + m1
heure_soir = "18:" + m2
heure_nuit_semaine = "23:" + m3
heure_nuit_week_end = "02:" + m3

heure_aléatoire1 = heure_aléatoire()
heure_aléatoire2 = heure_aléatoire()

################################################ DAILY MESSAGES ################################################

cls()

##### Planification des programmes #####

schedule.every().day.at(heure_matin).do(fonction_matin)
schedule.every().day.at(heure_soir).do(fonction_soir)
if jour != 4 or jour != 5:
    schedule.every().day.at(heure_nuit_semaine).do(fonction_nuit)
else:
    schedule.every().day.at(heure_nuit_week_end).do(fonction_nuit)
schedule.every().day.at(heure_aléatoire1).do(fonction_phrases_random)
schedule.every().day.at(heure_aléatoire2).do(fonction_anime_random)

########## Programme Principal #########

while True:
    
    schedule.run_pending()
    time.sleep(1)
    
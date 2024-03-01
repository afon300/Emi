import random
import os
import sys

sys.path.append(os.getcwd())
from api_gpt import *
from librairies_dico import *

chemin = os.path.join(os.getcwd(), "keys", "key_open_ai.txt")

################################################ BASIC FUNCTIONS ################################################

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def heure_aléatoire():
    aléheure = random.randint(0, 23)
    while (aléheure > 2 and aléheure < 9):
        aléheure = random.randint(0, 23)
    alémin = random.randint(0, 59)
    heure_formatee = str(aléheure).zfill(2)
    minute_formatee = str(alémin).zfill(2)
    heure_aléatoire = heure_formatee + ":" + minute_formatee
    return heure_aléatoire

def minutes_aléatoire():
    minutes_aléatoires1 = random.randint(0, 59)
    minute_formatee1 = str(minutes_aléatoires1).zfill(2)
    
    minutes_aléatoires2 = random.randint(0, 59)
    minute_formatee2 = str(minutes_aléatoires2).zfill(2)
    
    minutes_aléatoires3 = random.randint(0, 59)
    minute_formatee3 = str(minutes_aléatoires3).zfill(2)
    
    return minute_formatee1, minute_formatee2, minute_formatee3

def prompt():
    prompt1 = "Tu est une utilisatrice de Twitter, fan d'anime, tu a 16 ans, agis comme si tu avais une conversation normal entre toi et ton groupe, tu es gentille et attentionné, tu es un peu timide, fais des messages courts en moyenne 120 caractères dans le style des anime, tu parler à la 2e personne du pluriel quand tu pause des question. caractère, tu parle à tes amis, nous somme le"
    return prompt1

############################################### DAILY FUNCTIONS ##############################################


def fonction_matin(jour, temps, prompt1):
    dico_prompt_matin = dico_matin()            
    pl = True
    prompt2 = ""
    while pl == True:
        random_nb = random.randint(1, 13)
        if random_nb == 3 and jour == 5:
            pl = False
        if random_nb == 4 and jour == 6:
            pl = False
        if ((random_nb == 7 or random_nb == 8) and (jour != 5 and jour != 6)):
            pl = False
        if random_nb == 12 and jour == 4:
            pl = False
        if random_nb == 10 and jour == 6:
            pl = False
        if ((random_nb != 3) and (random_nb != 4) and (random_nb != 7) and (random_nb != 8) and (random_nb != 12) and (random_nb != 10)):
            pl = False
                
    for prompt_du_dico_matin, num in dico_prompt_matin.items():
        if num == random_nb:
            prompt2 = prompt_du_dico_matin
            break
    prompt = prompt1 + " " + str(temps) + " " + prompt2
    reponse = gpt(prompt, chemin)
    
    return reponse

def fonction_soir(jour, temps, prompt1):
    dico_prompt_soir = dico_soir()            
    pl = True
    prompt2 = ""
    while pl == True:
        random_nb = random.randint(1, 18)
        if random_nb == 16 and jour == 4:
            pl = False
        if random_nb == 17 and jour == 4:
            pl = False
        if random_nb != 16:
            pl = False
                
    for prompt_du_dico_soir, num in dico_prompt_soir.items():
        if num == random_nb:
            prompt2 = prompt_du_dico_soir
            break
    prompt = prompt1 + " " + str(temps) + " " + prompt2
    reponse = gpt(prompt, chemin)
        
    return reponse
    
def fonction_nuit(temps, prompt1):
    dico_prompt_nuit = dico_nuit()            
    random_nb = random.randint(1, 18)   
    prompt2 = ""      
    for prompt_du_dico_nuit, num in dico_prompt_nuit.items():
        if num == random_nb:
            prompt2 = prompt_du_dico_nuit
            break
    prompt = prompt1 + " " + str(temps) + " " + prompt2
    reponse = gpt(prompt, chemin)
    
    return reponse

def fonction_phrases_random(prompt1):
    dico_phrase = dico_phrases()            
    random_nb = random.randint(1, 76)   
    prompt2 = ""      
    for prompt_du_dico_random, num in dico_phrase.items():
        if num == random_nb:
            prompt2 = prompt_du_dico_random
            break
    prompt = prompt1 + " " + prompt2
    reponse = gpt(prompt, chemin)
    
    return reponse

def fonction_anime_random(prompt1):
    dico_anime_question = dico_question_anime_name()   
    dico_anime_nom = dico_nom_anime()  
    
    question_anime_aléatoire = random.randint(1, 15)        
    nom_anime_aléatoire = random.randint(1, 52)
    
    question = ""
    anime = ""    
    for question_anime, num in dico_anime_question.items():
        if num == question_anime_aléatoire:
            question = question_anime
            break

    for anime, num in dico_anime_nom.items():
        if num == nom_anime_aléatoire:
            nom_anime = anime
            break 
        
    prompt2 = question.format(anime=nom_anime)
    prompt = prompt1 + " " + prompt2
    reponse = gpt(prompt, chemin)
    
    return reponse
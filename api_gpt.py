import openai
from fonctions import *
    
def GPT(prompt):
    with open('key.txt', 'r') as f:
        clé_chiffré = f.read()
        clé_déchiffré = dechiffrer_cesar(clé_chiffré)
    openai.api_key = clé_déchiffré
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )

    reponse = (completion['choices'][0]['message']['content'])
        
    return reponse
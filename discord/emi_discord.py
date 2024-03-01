import discord
import sys
import os

from discord.ext import commands

sys.path.append(os.getcwd())
from api_gpt import *
from librairies_dico import *

intents = discord.Intents.default()
# Crée une instance du bot avec le préfixe de commande
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement pour indiquer que le bot est prêt
@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("----------------------")

# Commande pour répondre "True" lorsque l'utilisateur mentionne le bot avec une phrase
@bot.event
async def on_message(message): # Vérifie si le bot est mentionné et que ce n'est pas lui-même

    if bot.user.mentioned_in(message) and message.author != bot.user: # Récupère la mention de l'utilisateur
        author_mention = message.author.mention # Récupère le contenu du message après la mention du bot
        content = message.content.split('@emi')[1].strip() # Répond "True" à l'utilisateur
        await message.channel.send(f"{author_mention} True") # Appelle le gestionnaire d'événements on_message normal pour les autres fonctionnalités
    await bot.process_commands(message)

token_path = os.path.join(os.getcwd(), "discord", "key_discord.txt")
print(token_path)
with open(token_path, 'r') as f:
    clé_chiffré = f.read()
    clé_déchiffré = dechiffrer_cesar(clé_chiffré)
bot.run(clé_déchiffré)

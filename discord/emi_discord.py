import discord
import sys

from discord.ext import commands

sys.path.append(r'C:\Users\antoi\Documents\github\LaughWithGPT')
from api_gpt import *
from librairies_dico import *

# Crée une instance du bot avec le préfixe de commande
bot = commands.Bot(command_prefix='!')

# Événement pour indiquer que le bot est prêt
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Commande simple pour saluer un utilisateur
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

# Commande pour effacer un nombre spécifié de messages
@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

# Token du bot - REMARQUE : Remplacez 'YOUR_TOKEN_HERE' par le token de votre bot Discord
bot.run()

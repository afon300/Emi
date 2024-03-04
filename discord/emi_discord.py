import discord
import sys
import os

from discord.ext import commands

sys.path.append(os.getcwd())
from api_gpt import *
from librairies_dico import *

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("----------------------")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        await message.channel.send(f"Salut {message.author.mention}!")
        print(message)

    await bot.process_commands(message)

token_path = os.path.join(os.getcwd(), "keys", "key_discord.txt")
print(token_path)
with open(token_path, 'r') as f:
    clé_chiffré = f.read()
    clé_déchiffré = dechiffrer_cesar(clé_chiffré)
bot.run(clé_déchiffré)

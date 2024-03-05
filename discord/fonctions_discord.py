import discord
import sys
import os

from discord.ext import commands

sys.path.append(os.getcwd())
from api_gpt import *
from librairies_dico import *

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


############################################ FONCTIONS ############################################


async def process_discord_message(message):
    if message.author == bot.user:
        return
    content = message.content # contenu du message
    author = message.author # nom de l'auteur

    guild = message.guild # récupérer le serveur
    if guild is not None:
        guild_name = guild.name
    else:
        guild_name = "Message envoyé en dehors d'un serveur"

    channel_type = message.channel.type # type du channel
    is_bot_mention = bot.user in message.mentions and message.author.bot # si c'est un bot
    is_human_mention = bot.user in message.mentions and not message.author.bot #si c'est un humain

    print(f"Contenu du message : {content}")
    print(f"Auteur du message : {author}")
    print(f"Serveur : {guild_name}")
    print(f"Type de salon : {channel_type}")
    print(f"Mention par un bot : {is_bot_mention}")
    print(f"Mention par un humain : {is_human_mention}")

    await bot.process_commands(message)
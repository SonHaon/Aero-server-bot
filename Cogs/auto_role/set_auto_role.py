import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from .auto_role_buttons import *

import logging 
logger = logging.getLogger('discord.artichauds') 

class set_auto_role(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="set_auto_role",description="créer le message pour l'auto role")
    async def set_auto_role(self,interaction:discord.Interaction):
        embed = discord.Embed(title = "choisissez une couleur", description = "cliquez sur le bouton avoir la couleur")
        embed.set_footer(text = f"{interaction.guild.name}", icon_url=interaction.guild.icon.url)
        await interaction.channel.send(embed=embed,view=boutons_auto_role(interaction.guild))
        await interaction.response.send_message("l'auto role à bien été créer",ephemeral=True)
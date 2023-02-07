import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import os

import logging
logger = logging.getLogger('discord.artichauds')

from ..checks import check

class reboot(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="reboot",description="redémarre le bot et le mets a jour")
    @check.is_SonHaon()
    async def reboot(self,interaction:discord.Interaction):
        await self.bot.change_presence(status=discord.Status.offline)
        await interaction.response.send_message("le bot va redémarrer",ephemeral=True)
        os.system("systemctl restart discord-bot")
        
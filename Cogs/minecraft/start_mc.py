import discord 
from discord.ext import  commands 
from discord import  app_commands
from discord.ui import * 
import os
from ..checks import check


class start_mc(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="start_mc",description="lance le serveur minecraft")
    @check.is_modo()
    async def spam(self, interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        os.system(f'sudo systemctl start minecraft')
        await interaction.edit_original_response(content=f"le server démarre")
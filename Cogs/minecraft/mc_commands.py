import discord 
from discord.ext import  commands 
from discord import  app_commands
from discord.ui import * 
import os
from ..checks import check


class mc_commands(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="commands",description="execute une commande sur le serveur minecraft")
    @check.is_SonHaon()
    async def spam(self, interaction:discord.Interaction, commande:str):
        await interaction.response.defer(ephemeral=True)
        os.system(f'echo "{commande}" > /run/minecraft.stdin')
        interaction.edit_original_response(content=f"la commandes `{commande}` à bien été executé")
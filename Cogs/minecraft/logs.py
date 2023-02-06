import discord 
from discord.ext import  commands 
from discord import  app_commands
from discord.ui import * 
from ..checks import check


class logs(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="logs",description="montre les 20 dernière ligne de la console")
    @check.is_modo()
    async def spam(self, interaction:discord.Interaction, ligne:str):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content="cette commande est encore en cours de développement")
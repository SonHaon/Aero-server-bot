import discord 
from discord.ext import  commands 
from discord import  app_commands
from discord.ui import * 
import os
from ..checks import check

class minecraft(commands.GroupCog, name="minecraft"): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        super().__init__()

    @app_commands.command(name="commands",description="execute une commande sur le serveur minecraft")
    @check.is_SonHaon()
    async def commands(self, interaction:discord.Interaction, commande:str):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content=f"la commandes `{commande}` à bien été executé")


    @app_commands.command(name="start_mc",description="lance le serveur minecraft")
    @check.is_modo()
    async def start_mc(self, interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        os.system(f'sudo systemctl start minecraft')
        await interaction.edit_original_response(content=f"le server démarre")


    @app_commands.command(name="logs",description="montre les 20 dernière ligne de la console")
    @check.is_modo()
    async def spam(self, interaction:discord.Interaction, ligne:int=20):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content="cette commande est encore en cours de développement")
        with open("/home/sonhaon/minecraft/logs/latest.log","r",encoding="utf8") as file:
            lines = file.readlines()
        lines.reverse()
        for i in range(20):
            print(lines[i])
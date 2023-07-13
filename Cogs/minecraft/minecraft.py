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


    @app_commands.command(name="logs",description="montre les dernière ligne de la console")
    @check.is_modo()
    async def spam(self, interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        with open("/home/sonhaon/minecraft/logs/latest.log","r",encoding="utf8") as file:
            lines = file.readlines()
        lines.reverse()
        log=[]
        for i in range(100):
            log.append(lines[i])
            if "".join(log).count("") >= 2000:
                log.pop()
                break
        await interaction.edit_original_response(content=f"```{''.join(log)}```",file="/home/sonhaon/minecraft/logs/latest.log")

        